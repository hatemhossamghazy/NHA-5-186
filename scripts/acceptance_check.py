"""Dataset acceptance audit for deduped MegaVul and Big-Vul datasets."""

from __future__ import annotations

import argparse
import hashlib
import sys
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path

import pandas as pd

from languages import registry
from shield_core.datasets.dedupe import (
    NoCommentRemover,
    StrippingNormalizer,
    build_normalizers,
)

ROOT = Path(__file__).resolve().parents[1]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
DEFAULT_DATASETS = {
    "MegaVul": ROOT / "data" / "interim" / "megavul_deduped.parquet",
    "Big-Vul": ROOT / "data" / "interim" / "bigvul_deduped.parquet",
    "cvefixes_cpp": ROOT / "data" / "interim" / "cvefixes_cpp_deduped.parquet",
    "cvefixes_python": ROOT / "data" / "interim" / "cvefixes_python_deduped.parquet",
}

DEFAULT_REPORT = ROOT / "docs" / "dataset_audit.md"

RANDOM_SEED = 42
NOISE_SAMPLE_SIZE = 100

# These are candidate aliases, not mandatory schema definitions.
COLUMN_ALIASES = {
    "code": ["code", "code_snippet", "function", "func", "vulnerable_code"],
    "label": ["label", "target", "vul", "vulnerable", "is_vulnerable"],
    "language": ["language", "lang", "programming_language"],
    "cwe": ["cwe", "cwe_id", "weakness", "weakness_id"],
    "hash": ["normalized_hash", "code_hash", "hash"],
}

# Optional expected schema columns.
# If your project's schema.py defines SCHEMA_COLUMNS, the script
# will attempt to import it. Otherwise, it reports observed columns.
try:
    from shield_core.datasets.schema import SCHEMA_COLUMNS
except (ImportError, AttributeError):
    SCHEMA_COLUMNS = None


def resolve_column(df: pd.DataFrame, logical_name: str) -> str | None:
    """Find a column using known aliases."""
    lookup = {str(column).strip().lower(): column for column in df.columns}

    for alias in COLUMN_ALIASES[logical_name]:
        if alias.lower() in lookup:
            return lookup[alias.lower()]

    return None


NORMALIZERS = build_normalizers(registry.all_languages())
FALLBACK_NORMALIZER = StrippingNormalizer(NoCommentRemover())


def get_normalizer(language: object):
    """Return the normalizer configured for the given language."""
    if not isinstance(language, str):
        return FALLBACK_NORMALIZER
    return NORMALIZERS.get(language, FALLBACK_NORMALIZER)


def normalize_code(value: object, language: object = None) -> str:
    """Normalize code using the same logic as the deduplication pipeline."""
    if not isinstance(value, str):
        return ""
    return get_normalizer(language).normalize(value)


def code_hash(value: object, language: object = None) -> str:
    """Compute SHA-256 using the deduplication pipeline's normalization."""
    normalized = normalize_code(value, language)
    if not normalized:
        return ""

    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def read_dataset(path: Path) -> pd.DataFrame:
    """Read a Parquet dataset."""
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_parquet(path)


def find_code_hashes(
    df: pd.DataFrame,
    code_col: str | None,
    hash_col: str | None,
    language_col: str | None,
) -> pd.Series:
    """Use a supplied hash column or calculate language-aware code hashes."""
    if hash_col:
        supplied = df[hash_col].astype("string").fillna("").str.strip()
        return supplied

    if code_col:
        if language_col:
            return pd.Series(
                [
                    code_hash(code, language)
                    for code, language in zip(
                        df[code_col],
                        df[language_col],
                        strict=True,
                    )
                ],
                index=df.index,
                dtype="string",
            )

        return df[code_col].map(code_hash).astype("string")

    return pd.Series("", index=df.index, dtype="string")


def markdown_table(
    df: pd.DataFrame,
    empty_message: str = "No records.",
) -> str:
    """Render a DataFrame as a Markdown table."""
    if df.empty:
        return empty_message

    return df.to_markdown(index=False)


def inspect_dataset(
    name: str,
    path: Path,
    df: pd.DataFrame,
) -> dict:
    """Run structural and label checks for one dataset."""
    code_col = resolve_column(df, "code")
    label_col = resolve_column(df, "label")
    language_col = resolve_column(df, "language")
    cwe_col = resolve_column(df, "cwe")
    hash_col = resolve_column(df, "hash")

    missing_counts = df.isna().sum()

    missing_table = pd.DataFrame(
        {
            "column": df.columns,
            "missing_count": [int(missing_counts[c]) for c in df.columns],
            "missing_pct": [
                round(float(missing_counts[c]) / max(len(df), 1) * 100, 3) for c in df.columns
            ],
        }
    )

    # Empty strings are checked separately from null values.
    empty_string_counts = {}
    for column in df.columns:
        if pd.api.types.is_object_dtype(df[column]) or pd.api.types.is_string_dtype(df[column]):
            empty_string_counts[column] = int(df[column].astype("string").str.strip().eq("").sum())

    label_counts = Counter()
    invalid_label_count = None
    valid_binary_labels = None

    if label_col:
        labels = df[label_col]
        label_counts = Counter(labels.astype("string").fillna("<NULL>"))

        non_null_labels = set(labels.dropna().astype(str).str.strip())
        valid_binary_labels = non_null_labels.issubset({"0", "1", "0.0", "1.0"})
        invalid_label_count = int(
            (~labels.astype("string").str.strip().isin(["0", "1", "0.0", "1.0"])).sum()
        )

    required_columns = list(SCHEMA_COLUMNS) if SCHEMA_COLUMNS else []
    missing_required = sorted(set(required_columns) - set(df.columns))

    hashes = find_code_hashes(df, code_col, hash_col, language_col)
    nonempty_hashes = hashes[hashes.ne("")]

    duplicate_hash_rows = int(nonempty_hashes.duplicated(keep=False).sum())
    unique_hash_count = int(nonempty_hashes.nunique())

    if code_col and language_col:
        normalized_codes = [
            normalize_code(code, language)
            for code, language in zip(
                df[code_col],
                df[language_col],
                strict=True,
            )
        ]
        empty_code_count = sum(not code for code in normalized_codes)
    elif code_col:
        empty_code_count = int(df[code_col].map(normalize_code).eq("").sum())
    else:
        empty_code_count = None

    summary = {
        "dataset": name,
        "path": str(path),
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "column_names": list(map(str, df.columns)),
        "code_col": code_col,
        "label_col": label_col,
        "language_col": language_col,
        "cwe_col": cwe_col,
        "hash_col": hash_col,
        "unique_hashes": unique_hash_count,
        "duplicate_hash_rows": duplicate_hash_rows,
        "empty_code_count": empty_code_count,
        "missing_required_columns": missing_required,
        "missing_table": missing_table,
        "empty_string_counts": empty_string_counts,
        "label_counts": dict(label_counts),
        "invalid_label_count": invalid_label_count,
        "valid_binary_labels": valid_binary_labels,
        "hashes": hashes,
    }

    return summary


def build_language_cwe_matrix(
    df: pd.DataFrame,
    language_col: str | None,
    cwe_col: str | None,
    label_col: str | None,
) -> pd.DataFrame:
    columns = [
        "language",
        "cwe",
        "total_samples",
        "vulnerable_samples",
    ]

    if not language_col or not cwe_col or not label_col:
        return pd.DataFrame(columns=columns)

    def extract_cwes(value: object) -> list[str]:
        if value is None:
            return []

        if isinstance(value, str):
            values = [value]
        elif isinstance(value, (list, tuple, set)):
            values = list(value)
        elif hasattr(value, "tolist"):
            values = value.tolist()
            if not isinstance(values, list):
                values = [values]
        else:
            values = [value]

        result = []
        for item in values:
            if item is None or pd.isna(item):
                continue

            cwe = str(item).strip()
            if cwe and cwe != "[]" and cwe.lower() != "nan":
                result.append(cwe)

        return list(dict.fromkeys(result))

    work = pd.DataFrame(
        {
            "language": df[language_col].astype("string").fillna("<MISSING>"),
            "cwes": df[cwe_col].map(extract_cwes),
            "is_vulnerable": pd.to_numeric(df[label_col], errors="coerce").eq(1).astype(int),
        },
        index=df.index,
    )

    # Count every sample with a missing or empty CWE under an explicit category.
    work["cwes"] = work["cwes"].map(lambda values: values if values else ["<MISSING>"])

    # One row per sample/CWE pair, so multi-CWE samples count toward each CWE.
    work = work.explode("cwes").rename(columns={"cwes": "cwe"})

    result = (
        work.groupby(["language", "cwe"], dropna=False)
        .agg(
            total_samples=("is_vulnerable", "size"),
            vulnerable_samples=("is_vulnerable", "sum"),
        )
        .reset_index()
    )

    return result.sort_values(
        ["language", "vulnerable_samples", "total_samples"],
        ascending=[True, False, False],
    ).reset_index(drop=True)


def find_conflict_groups(
    df: pd.DataFrame,
    summary: dict,
) -> pd.DataFrame:
    """Find identical hashes associated with multiple labels."""
    code_col = summary["code_col"]
    label_col = summary["label_col"]
    hash_col = summary["hash_col"]

    if not label_col:
        return pd.DataFrame(columns=["hash", "row_count", "labels", "sample_indices"])

    hashes = find_code_hashes(df, code_col, hash_col, summary["language_col"])

    work = pd.DataFrame(
        {
            "hash": hashes,
            "label": df[label_col].astype("string").fillna("<NULL>"),
        },
        index=df.index,
    )

    work = work[work["hash"].ne("")]

    grouped = work.groupby("hash", sort=False).agg(
        row_count=("label", "size"),
        labels=("label", lambda values: sorted(set(values))),
        sample_indices=("label", lambda values: list(values.index[:5])),
    )

    conflicts = grouped[grouped["labels"].map(len) > 1].reset_index()

    return conflicts


def compute_overlap(
    dataset_summaries: dict[str, dict],
) -> tuple[pd.DataFrame, dict]:
    """Calculate pairwise overlap using each dataset's selected hash strategy."""
    rows = []
    unique_hash_sets = {}

    for name, summary in dataset_summaries.items():
        hashes = summary["hashes"]
        unique_hash_sets[name] = set(hashes[hashes.ne("")].tolist())

    for left, right in combinations(unique_hash_sets, 2):
        left_hashes = unique_hash_sets[left]
        right_hashes = unique_hash_sets[right]
        shared = left_hashes & right_hashes

        rows.append(
            {
                "dataset_a": left,
                "dataset_b": right,
                "unique_hashes_a": len(left_hashes),
                "unique_hashes_b": len(right_hashes),
                "shared_hashes": len(shared),
                "overlap_pct_a": round(100 * len(shared) / max(len(left_hashes), 1), 3),
                "overlap_pct_b": round(100 * len(shared) / max(len(right_hashes), 1), 3),
            }
        )

    return pd.DataFrame(rows), unique_hash_sets


def sample_label_noise(
    dataset_name: str,
    df: pd.DataFrame,
    summary: dict,
    sample_size: int,
    seed: int,
    output_path: Path,
) -> dict:
    """Export a reproducible random sample of conflicting groups for manual review."""
    conflicts = find_conflict_groups(df, summary)

    if conflicts.empty:
        return {
            "dataset": dataset_name,
            "conflict_groups": 0,
            "sampled_groups": 0,
            "sample_path": None,
        }

    sample = conflicts.sample(
        n=min(sample_size, len(conflicts)),
        random_state=seed,
    ).copy()

    code_col = summary["code_col"]
    label_col = summary["label_col"]
    language_col = summary["language_col"]
    cwe_col = summary["cwe_col"]

    hashes = find_code_hashes(
        df,
        summary["code_col"],
        summary["hash_col"],
        summary["language_col"],
    )

    rows = []

    for _, conflict in sample.iterrows():
        target_hash = conflict["hash"]
        matching_indices = hashes.index[hashes.eq(target_hash)].tolist()

        for index in matching_indices:
            row = {
                "dataset": dataset_name,
                "hash": target_hash,
                "row_index": index,
                "labels_in_conflict_group": ", ".join(conflict["labels"]),
                "group_row_count": int(conflict["row_count"]),
            }

            if label_col:
                row["label"] = df.at[index, label_col]

            if language_col:
                row["language"] = df.at[index, language_col]

            if cwe_col:
                row["cwe"] = df.at[index, cwe_col]

            if code_col:
                # Keep the full code so reviewers can inspect the actual case.
                row["code"] = df.at[index, code_col]

            rows.append(row)

    review_df = pd.DataFrame(rows)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    review_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    return {
        "dataset": dataset_name,
        "conflict_groups": int(len(conflicts)),
        "sampled_groups": int(len(sample)),
        "sample_path": str(output_path),
    }


def create_report(
    output_path: Path,
    summaries: dict[str, dict],
    matrices: list[pd.DataFrame],
    overlaps: pd.DataFrame,
    noise_results: list[dict],
) -> None:
    """Generate the Markdown audit report."""
    lines = [
        "# Dataset Acceptance Audit — D22",
        "",
        f"- Generated at (UTC): {datetime.now(timezone.utc).isoformat()}",
        "- Scope: deduped MegaVul and Big-Vul only.",
        "- This report does not claim acceptance for datasets that were not audited.",
        "",
        "## 1. Dataset Summary",
        "",
        (
            "| Dataset | Rows | Columns | Unique hashes | "
            "Rows in duplicate-hash groups | Empty code rows |"
        ),
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, summary in summaries.items():
        empty_code = (
            str(summary["empty_code_count"])
            if summary["empty_code_count"] is not None
            else "NOT CHECKED: code column not found"
        )
        lines.append(
            f"| {name} | {summary['rows']} | {len(summary['column_names'])} "
            f"| {summary['unique_hashes']} | {summary['duplicate_hash_rows']} "
            f"| {empty_code} |"
        )

    lines.extend(
        [
            "",
            "## 2. Structural and Data-Quality Checks",
            "",
        ]
    )

    for name, summary in summaries.items():
        lines.extend(
            [
                f"### {name}",
                "",
                f"- File: `{summary['path']}`",
                f"- Detected code column: `{summary['code_col']}`",
                f"- Detected label column: `{summary['label_col']}`",
                f"- Detected language column: `{summary['language_col']}`",
                f"- Detected CWE column: `{summary['cwe_col']}`",
                f"- Detected hash column: `{summary['hash_col']}`",
                f"- Missing required schema columns: `{summary['missing_required_columns']}`",
                f"- Valid binary labels (0/1): `{summary['valid_binary_labels']}`",
                f"- Invalid or missing labels: `{summary['invalid_label_count']}`",
                "",
                "#### Missing values by column",
                "",
                markdown_table(summary["missing_table"]),
                "",
                "#### Empty strings by column",
                "",
                markdown_table(
                    pd.DataFrame(
                        [
                            {"column": col, "empty_strings": count}
                            for col, count in summary["empty_string_counts"].items()
                        ]
                    )
                ),
                "",
                "#### Label distribution",
                "",
                markdown_table(
                    pd.DataFrame(
                        [
                            {"label": label, "count": count}
                            for label, count in summary["label_counts"].items()
                        ]
                    )
                ),
                "",
            ]
        )

    lines.extend(
        [
            "## 3. Language × CWE Count Matrix",
            "",
            "Counts are calculated from the available language and CWE columns. "
            "Vulnerable counts assume label 1 means vulnerable; verify this convention "
            "against the project dataset documentation.",
            "",
        ]
    )

    if matrices:
        matrix_df = pd.concat(matrices, ignore_index=True)
        lines.append(markdown_table(matrix_df))
    else:
        lines.append("No count matrix could be generated.")

    lines.extend(
        [
            "",
            "## 4. Label Noise Findings",
            "",
            "Conflicting groups are groups where the same selected hash has more than "
            "one distinct label. They require manual review; a conflict alone does "
            "not prove that a label is wrong.",
            "",
            "| Dataset | Conflict groups | Random groups exported | Review CSV |",
            "|---|---:|---:|---|",
        ]
    )

    for result in noise_results:
        lines.append(
            f"| {result['dataset']} | {result['conflict_groups']} "
            f"| {result['sampled_groups']} "
            f"| `{result['sample_path'] or 'None'}` |"
        )

    lines.extend(
        [
            "",
            "**Manual review status:** NOT COMPLETED BY THIS SCRIPT.",
            "",
            "Open each review CSV, inspect the code, label, CWE, and source context, "
            "then record the manually confirmed findings here. Do not treat the "
            "number of conflicting groups as the number of confirmed label errors.",
            "",
            "## 5. Cross-Dataset Overlap",
            "",
        ]
    )

    if overlaps.empty:
        lines.append("No pairwise overlap results were available.")
    else:
        lines.append(markdown_table(overlaps))

    lines.extend(
        [
            "",
            "Overlap is based on the selected hash column when present; otherwise, "
            "it is based on SHA-256 using the language-specific normalizers from "
            "the deduplication pipeline. For the final deduped files, zero shared "
            "hashes is expected because cross-dataset duplicates were removed "
            "during deduplication.",
            "",
            "## 6. Recommended CWE List per Language",
            "",
            "The table below ranks CWE groups by vulnerable sample count. It is a "
            "candidate list, not an automatic acceptance decision. Apply the project's "
            "official D22 threshold and verify the label convention before selecting "
            "CWE groups for downstream experiments.",
            "",
        ]
    )

    if matrices:
        matrix_df = pd.concat(matrices, ignore_index=True)

        ranked = matrix_df[matrix_df["cwe"].ne("<MISSING>")].copy()

        if not ranked.empty:
            ranked = ranked.sort_values(
                ["language", "vulnerable_samples"],
                ascending=[True, False],
            )

            ranked["rank_within_dataset_language"] = ranked.groupby("language").cumcount() + 1

        lines.append(markdown_table(ranked))
    else:
        lines.append("No recommendations available because the matrix is missing.")

    lines.extend(
        [
            "",
            "## 7. Acceptance Verdict",
            "",
            "| Dataset | Verdict | Reason |",
            "|---|---|---|",
        ]
    )

    for name, summary in summaries.items():
        reasons = []

        if summary["missing_required_columns"]:
            reasons.append("required schema columns missing")

        if summary["code_col"] is None:
            reasons.append("code column not detected")

        if summary["label_col"] is None:
            reasons.append("label column not detected")
        elif summary["valid_binary_labels"] is False or summary["invalid_label_count"] > 0:
            reasons.append("invalid or missing labels found")

        if summary["language_col"] is None:
            reasons.append("language column not detected")

        if summary["cwe_col"] is None:
            reasons.append("CWE column not detected")

        if summary["duplicate_hash_rows"] > 0:
            reasons.append("duplicate hashes remain; investigate")

        if reasons:
            verdict = "REVIEW"
            reason_text = "; ".join(reasons)
        else:
            verdict = "PRELIMINARY PASS"
            reason_text = (
                "basic automated checks passed; official D22 thresholds and "
                "manual label-noise review still need confirmation"
            )

        lines.append(f"| {name} | {verdict} | {reason_text} |")

    lines.extend(
        [
            "",
            "### Scope and Limitations",
            "",
            "- Only MegaVul and Big-Vul were audited.",
            "- This report does not provide a verdict for the other project datasets(python).",
            "- Manual label-noise review is still required.",
            "- Official D22 acceptance thresholds must be checked against project docs.",
            "",
        ]
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit deduped MegaVul and Big-Vul Parquet datasets."
    )

    parser.add_argument(
        "--megavul",
        type=Path,
        default=DEFAULT_DATASETS["MegaVul"],
        help="Path to deduped MegaVul Parquet file.",
    )
    parser.add_argument(
        "--bigvul",
        type=Path,
        default=DEFAULT_DATASETS["Big-Vul"],
        help="Path to deduped Big-Vul Parquet file.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT,
        help="Output Markdown report path.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=NOISE_SAMPLE_SIZE,
        help="Number of conflicting hash groups sampled per dataset.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=RANDOM_SEED,
        help="Random seed for reproducible label-conflict sampling.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    datasets = DEFAULT_DATASETS.copy()

    datasets["MegaVul"] = args.megavul
    datasets["Big-Vul"] = args.bigvul

    summaries = {}
    dataframes = {}
    matrices = []
    noise_results = []

    for name, path in datasets.items():
        print(f"[INFO] Reading {name}: {path}")

        if not path.exists():
            print(f"[WARNING] Skipping {name}: file not found at {path}")
            continue

        df = read_dataset(path)

        summary = inspect_dataset(name, path, df)
        summaries[name] = summary
        dataframes[name] = df

        matrix = build_language_cwe_matrix(
            df,
            summary["language_col"],
            summary["cwe_col"],
            summary["label_col"],
        )

        matrix.insert(0, "dataset", name)
        matrices.append(matrix)

        noise_csv = args.report.parent / f"{name.lower().replace('-', '')}_label_noise_sample.csv"

        noise_results.append(
            sample_label_noise(
                dataset_name=name,
                df=df,
                summary=summary,
                sample_size=args.sample_size,
                seed=args.seed,
                output_path=noise_csv,
            )
        )

        print(
            f"[INFO] {name}: rows={len(df):,}, "
            f"unique_hashes={summary['unique_hashes']:,}, "
            f"conflict_groups={noise_results[-1]['conflict_groups']:,}"
        )

    overlaps, _ = compute_overlap(summaries)

    create_report(
        output_path=args.report,
        summaries=summaries,
        matrices=matrices,
        overlaps=overlaps,
        noise_results=noise_results,
    )

    print(f"\n[DONE] Audit report created: {args.report}")
    print("[INFO] Review the generated CSV files for manual label-noise inspection.")
    print("[INFO] Update the report with manual findings before final submission.")


if __name__ == "__main__":
    main()
