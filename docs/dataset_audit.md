# Dataset Acceptance Audit — D22

- Generated at (UTC): 2026-10-10T12:30:53.188462+00:00
- Scope: deduped MegaVul and Big-Vul only.
- This report does not claim acceptance for datasets that were not audited.

## 1. Dataset Summary

| Dataset | Rows | Columns | Unique hashes | Rows in duplicate-hash groups | Empty code rows |
|---|---:|---:|---:|---:|---:|
| MegaVul | 336896 | 8 | 336896 | 0 | 0 |
| Big-Vul | 103349 | 8 | 103349 | 0 | 0 |

## 2. Structural and Data-Quality Checks

### MegaVul

- File: `D:\DEPI\NHA-5-186\data\interim\megavul_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |          320208 |        95.047 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       1 |   16688 |
|       0 |  320208 |

### Big-Vul

- File: `D:\DEPI\NHA-5-186\data\interim\bigvul_deduped.parquet`
- Detected code column: `code`
- Detected label column: `label`
- Detected language column: `language`
- Detected CWE column: `cwe`
- Detected hash column: `None`
- Missing required schema columns: `[]`
- Valid binary labels (0/1): `True`
- Invalid or missing labels: `0`

#### Missing values by column

| column     |   missing_count |   missing_pct |
|:-----------|----------------:|--------------:|
| code       |               0 |         0     |
| language   |               0 |         0     |
| label      |               0 |         0     |
| cwe        |               0 |         0     |
| project    |               0 |         0     |
| commit     |               0 |         0     |
| fixed_code |           97477 |        94.318 |
| source     |               0 |         0     |

#### Empty strings by column

| column     |   empty_strings |
|:-----------|----------------:|
| code       |               0 |
| language   |               0 |
| cwe        |               0 |
| project    |               0 |
| commit     |               0 |
| fixed_code |               0 |
| source     |               0 |

#### Label distribution

|   label |   count |
|--------:|--------:|
|       0 |   97477 |
|       1 |    5872 |

## 3. Language × CWE Count Matrix

Counts are calculated from the available language and CWE columns. Vulnerable counts assume label 1 means vulnerable; verify this convention against the project dataset documentation.

| dataset   | language   | cwe       |   total_samples |   vulnerable_samples |
|:----------|:-----------|:----------|----------------:|---------------------:|
| MegaVul   | cpp        | CWE-119   |           26407 |                 1591 |
| MegaVul   | cpp        | CWE-787   |           28139 |                 1518 |
| MegaVul   | cpp        | CWE-125   |           23588 |                 1453 |
| MegaVul   | cpp        | <MISSING> |           31418 |                 1402 |
| MegaVul   | cpp        | CWE-476   |           26969 |                 1290 |
| MegaVul   | cpp        | CWE-20    |           19452 |                 1074 |
| MegaVul   | cpp        | CWE-416   |           24602 |                 1007 |
| MegaVul   | cpp        | CWE-190   |           11789 |                  711 |
| MegaVul   | cpp        | CWE-200   |           11802 |                  561 |
| MegaVul   | cpp        | CWE-362   |           10623 |                  509 |
| MegaVul   | cpp        | CWE-399   |            9986 |                  440 |
| MegaVul   | cpp        | CWE-264   |            9541 |                  426 |
| MegaVul   | cpp        | CWE-120   |            6658 |                  424 |
| MegaVul   | cpp        | CWE-400   |            6223 |                  313 |
| MegaVul   | cpp        | CWE-189   |            6006 |                  296 |
| MegaVul   | cpp        | CWE-401   |           11501 |                  280 |
| MegaVul   | cpp        | CWE-617   |            4040 |                  261 |
| MegaVul   | cpp        | CWE-835   |            5081 |                  252 |
| MegaVul   | cpp        | CWE-415   |            6091 |                  184 |
| MegaVul   | cpp        | CWE-369   |            2510 |                  178 |
| MegaVul   | cpp        | CWE-772   |            2974 |                  174 |
| MegaVul   | cpp        | CWE-22    |            3760 |                  157 |
| MegaVul   | cpp        | CWE-254   |            2872 |                  128 |
| MegaVul   | cpp        | CWE-674   |            1985 |                  123 |
| MegaVul   | cpp        | CWE-122   |            2090 |                  115 |
| MegaVul   | cpp        | CWE-908   |            1817 |                  103 |
| MegaVul   | cpp        | CWE-59    |            1747 |                   95 |
| MegaVul   | cpp        | CWE-770   |            2022 |                   94 |
| MegaVul   | cpp        | CWE-287   |            1626 |                   94 |
| MegaVul   | cpp        | CWE-284   |            1452 |                   93 |
| MegaVul   | cpp        | CWE-834   |            4158 |                   88 |
| MegaVul   | cpp        | CWE-310   |            1302 |                   80 |
| MegaVul   | cpp        | CWE-909   |            1327 |                   78 |
| MegaVul   | cpp        | CWE-74    |            2384 |                   73 |
| MegaVul   | cpp        | CWE-295   |            1944 |                   71 |
| MegaVul   | cpp        | CWE-269   |            1013 |                   70 |
| MegaVul   | cpp        | CWE-667   |            1421 |                   69 |
| MegaVul   | cpp        | CWE-17    |            1002 |                   65 |
| MegaVul   | cpp        | CWE-193   |             889 |                   64 |
| MegaVul   | cpp        | CWE-78    |            1296 |                   60 |
| MegaVul   | cpp        | CWE-459   |             660 |                   60 |
| MegaVul   | cpp        | CWE-404   |            1748 |                   59 |
| MegaVul   | cpp        | CWE-843   |            1094 |                   59 |
| MegaVul   | cpp        | CWE-754   |             930 |                   58 |
| MegaVul   | cpp        | CWE-79    |             914 |                   58 |
| MegaVul   | cpp        | CWE-732   |             829 |                   58 |
| MegaVul   | cpp        | CWE-19    |            1271 |                   55 |
| MegaVul   | cpp        | CWE-681   |             704 |                   52 |
| MegaVul   | cpp        | CWE-863   |            1229 |                   49 |
| MegaVul   | cpp        | CWE-755   |            1048 |                   42 |
| MegaVul   | cpp        | CWE-252   |             526 |                   42 |
| MegaVul   | cpp        | CWE-665   |            1032 |                   40 |
| MegaVul   | cpp        | CWE-89    |            1743 |                   37 |
| MegaVul   | cpp        | CWE-668   |             853 |                   35 |
| MegaVul   | cpp        | CWE-129   |             726 |                   34 |
| MegaVul   | cpp        | CWE-203   |             737 |                   33 |
| MegaVul   | cpp        | CWE-367   |             952 |                   32 |
| MegaVul   | cpp        | CWE-704   |             748 |                   32 |
| MegaVul   | cpp        | CWE-682   |             581 |                   32 |
| MegaVul   | cpp        | CWE-131   |             528 |                   32 |
| MegaVul   | cpp        | CWE-1284  |             368 |                   32 |
| MegaVul   | cpp        | CWE-330   |             504 |                   31 |
| MegaVul   | cpp        | CWE-862   |             459 |                   30 |
| MegaVul   | cpp        | CWE-354   |             445 |                   30 |
| MegaVul   | cpp        | CWE-763   |             439 |                   30 |
| MegaVul   | cpp        | CWE-134   |            1055 |                   28 |
| MegaVul   | cpp        | CWE-191   |             817 |                   27 |
| MegaVul   | cpp        | CWE-824   |             507 |                   25 |
| MegaVul   | cpp        | CWE-327   |             314 |                   25 |
| MegaVul   | cpp        | CWE-276   |             674 |                   24 |
| MegaVul   | cpp        | CWE-77    |             418 |                   24 |
| MegaVul   | cpp        | CWE-121   |             233 |                   23 |
| MegaVul   | cpp        | CWE-502   |             113 |                   22 |
| MegaVul   | cpp        | CWE-212   |             291 |                   21 |
| MegaVul   | cpp        | CWE-697   |             239 |                   21 |
| MegaVul   | cpp        | CWE-345   |             196 |                   20 |
| MegaVul   | cpp        | CWE-94    |             396 |                   19 |
| MegaVul   | cpp        | CWE-436   |             281 |                   19 |
| MegaVul   | cpp        | CWE-611   |             240 |                   18 |
| MegaVul   | cpp        | CWE-444   |             186 |                   18 |
| MegaVul   | cpp        | CWE-326   |             157 |                   18 |
| MegaVul   | cpp        | CWE-662   |             111 |                   18 |
| MegaVul   | cpp        | CWE-776   |              81 |                   18 |
| MegaVul   | cpp        | CWE-434   |             574 |                   16 |
| MegaVul   | cpp        | CWE-116   |             455 |                   15 |
| MegaVul   | cpp        | CWE-601   |             216 |                   15 |
| MegaVul   | cpp        | CWE-672   |              81 |                   13 |
| MegaVul   | cpp        | CWE-347   |             101 |                   12 |
| MegaVul   | cpp        | CWE-440   |             636 |                   11 |
| MegaVul   | cpp        | CWE-426   |             201 |                   10 |
| MegaVul   | cpp        | CWE-613   |              44 |                   10 |
| MegaVul   | cpp        | CWE-197   |              35 |                   10 |
| MegaVul   | cpp        | CWE-552   |             338 |                    9 |
| MegaVul   | cpp        | CWE-384   |             217 |                    9 |
| MegaVul   | cpp        | CWE-319   |             166 |                    9 |
| MegaVul   | cpp        | CWE-306   |             113 |                    9 |
| MegaVul   | cpp        | CWE-1021  |             501 |                    8 |
| MegaVul   | cpp        | CWE-346   |             232 |                    8 |
| MegaVul   | cpp        | CWE-670   |             170 |                    8 |
| MegaVul   | cpp        | CWE-388   |             123 |                    8 |
| MegaVul   | cpp        | CWE-918   |             103 |                    8 |
| MegaVul   | cpp        | CWE-290   |              79 |                    8 |
| MegaVul   | cpp        | CWE-913   |              46 |                    8 |
| MegaVul   | cpp        | CWE-428   |             106 |                    7 |
| MegaVul   | cpp        | CWE-911   |             102 |                    7 |
| MegaVul   | cpp        | CWE-532   |             127 |                    6 |
| MegaVul   | cpp        | CWE-90    |              91 |                    6 |
| MegaVul   | cpp        | CWE-407   |              59 |                    6 |
| MegaVul   | cpp        | CWE-331   |              38 |                    6 |
| MegaVul   | cpp        | CWE-18    |              36 |                    6 |
| MegaVul   | cpp        | CWE-385   |              18 |                    6 |
| MegaVul   | cpp        | CWE-693   |             328 |                    5 |
| MegaVul   | cpp        | CWE-680   |             143 |                    5 |
| MegaVul   | cpp        | CWE-823   |             114 |                    5 |
| MegaVul   | cpp        | CWE-1187  |              78 |                    5 |
| MegaVul   | cpp        | CWE-126   |              26 |                    5 |
| MegaVul   | cpp        | CWE-337   |              21 |                    5 |
| MegaVul   | cpp        | CWE-409   |              17 |                    5 |
| MegaVul   | cpp        | CWE-427   |             360 |                    4 |
| MegaVul   | cpp        | CWE-16    |             309 |                    4 |
| MegaVul   | cpp        | CWE-285   |             191 |                    4 |
| MegaVul   | cpp        | CWE-273   |             161 |                    4 |
| MegaVul   | cpp        | CWE-1077  |             100 |                    4 |
| MegaVul   | cpp        | CWE-522   |              67 |                    4 |
| MegaVul   | cpp        | CWE-626   |              55 |                    4 |
| MegaVul   | cpp        | CWE-88    |              28 |                    4 |
| MegaVul   | cpp        | CWE-338   |              22 |                    4 |
| MegaVul   | cpp        | CWE-241   |              21 |                    4 |
| MegaVul   | cpp        | CWE-1188  |             260 |                    3 |
| MegaVul   | cpp        | CWE-706   |             146 |                    3 |
| MegaVul   | cpp        | CWE-229   |             113 |                    3 |
| MegaVul   | cpp        | CWE-494   |              48 |                    3 |
| MegaVul   | cpp        | CWE-325   |              39 |                    3 |
| MegaVul   | cpp        | CWE-118   |              32 |                    3 |
| MegaVul   | cpp        | CWE-172   |              17 |                    3 |
| MegaVul   | cpp        | CWE-707   |              16 |                    3 |
| MegaVul   | cpp        | CWE-639   |             116 |                    2 |
| MegaVul   | cpp        | CWE-307   |              34 |                    2 |
| MegaVul   | cpp        | CWE-838   |              34 |                    2 |
| MegaVul   | cpp        | CWE-320   |              23 |                    2 |
| MegaVul   | cpp        | CWE-113   |              17 |                    2 |
| MegaVul   | cpp        | CWE-924   |              12 |                    2 |
| MegaVul   | cpp        | CWE-255   |               8 |                    2 |
| MegaVul   | cpp        | CWE-762   |               7 |                    2 |
| MegaVul   | cpp        | CWE-1333  |               3 |                    2 |
| MegaVul   | cpp        | CWE-250   |             587 |                    1 |
| MegaVul   | cpp        | CWE-312   |             187 |                    1 |
| MegaVul   | cpp        | CWE-460   |              89 |                    1 |
| MegaVul   | cpp        | CWE-1050  |              75 |                    1 |
| MegaVul   | cpp        | CWE-358   |              66 |                    1 |
| MegaVul   | cpp        | CWE-248   |              60 |                    1 |
| MegaVul   | cpp        | CWE-349   |              60 |                    1 |
| MegaVul   | cpp        | CWE-300   |              56 |                    1 |
| MegaVul   | cpp        | CWE-943   |              56 |                    1 |
| MegaVul   | cpp        | CWE-93    |              47 |                    1 |
| MegaVul   | cpp        | CWE-282   |              31 |                    1 |
| MegaVul   | cpp        | CWE-23    |              27 |                    1 |
| MegaVul   | cpp        | CWE-26    |              27 |                    1 |
| MegaVul   | cpp        | CWE-361   |              27 |                    1 |
| MegaVul   | cpp        | CWE-788   |              23 |                    1 |
| MegaVul   | cpp        | CWE-335   |              22 |                    1 |
| MegaVul   | cpp        | CWE-590   |              22 |                    1 |
| MegaVul   | cpp        | CWE-475   |              21 |                    1 |
| MegaVul   | cpp        | CWE-352   |              17 |                    1 |
| MegaVul   | cpp        | CWE-628   |              15 |                    1 |
| MegaVul   | cpp        | CWE-323   |              12 |                    1 |
| MegaVul   | cpp        | CWE-73    |              11 |                    1 |
| MegaVul   | cpp        | CWE-117   |               9 |                    1 |
| MegaVul   | cpp        | CWE-185   |               8 |                    1 |
| MegaVul   | cpp        | CWE-1049  |               7 |                    1 |
| MegaVul   | cpp        | CWE-610   |               7 |                    1 |
| MegaVul   | cpp        | CWE-202   |               3 |                    1 |
| MegaVul   | cpp        | CWE-324   |               2 |                    1 |
| MegaVul   | cpp        | CWE-209   |               1 |                    1 |
| MegaVul   | cpp        | CWE-208   |               5 |                    0 |
| Big-Vul   | cpp        | <MISSING> |           24363 |                 1473 |
| Big-Vul   | cpp        | CWE-119   |           13556 |                 1064 |
| Big-Vul   | cpp        | CWE-20    |           12631 |                  617 |
| Big-Vul   | cpp        | CWE-399   |            8627 |                  481 |
| Big-Vul   | cpp        | CWE-125   |            3256 |                  263 |
| Big-Vul   | cpp        | CWE-200   |            3835 |                  233 |
| Big-Vul   | cpp        | CWE-264   |            5463 |                  203 |
| Big-Vul   | cpp        | CWE-416   |            5717 |                  178 |
| Big-Vul   | cpp        | CWE-189   |            3128 |                  168 |
| Big-Vul   | cpp        | CWE-362   |            2593 |                  142 |
| Big-Vul   | cpp        | CWE-190   |            1921 |                  136 |
| Big-Vul   | cpp        | CWE-787   |            1592 |                  101 |
| Big-Vul   | cpp        | CWE-284   |            1279 |                   95 |
| Big-Vul   | cpp        | CWE-254   |            2094 |                   78 |
| Big-Vul   | cpp        | CWE-476   |            1891 |                   57 |
| Big-Vul   | cpp        | CWE-415   |             321 |                   42 |
| Big-Vul   | cpp        | CWE-310   |             602 |                   40 |
| Big-Vul   | cpp        | CWE-732   |            1119 |                   38 |
| Big-Vul   | cpp        | CWE-19    |             363 |                   37 |
| Big-Vul   | cpp        | CWE-404   |             700 |                   34 |
| Big-Vul   | cpp        | CWE-79    |             545 |                   32 |
| Big-Vul   | cpp        | CWE-22    |             479 |                   25 |
| Big-Vul   | cpp        | CWE-59    |             547 |                   22 |
| Big-Vul   | cpp        | CWE-285   |             369 |                   22 |
| Big-Vul   | cpp        | CWE-772   |             177 |                   21 |
| Big-Vul   | cpp        | CWE-835   |             440 |                   19 |
| Big-Vul   | cpp        | CWE-269   |             277 |                   18 |
| Big-Vul   | cpp        | CWE-134   |             547 |                   16 |
| Big-Vul   | cpp        | CWE-17    |             275 |                   16 |
| Big-Vul   | cpp        | CWE-311   |             164 |                   16 |
| Big-Vul   | cpp        | CWE-358   |              48 |                   14 |
| Big-Vul   | cpp        | CWE-704   |             475 |                   13 |
| Big-Vul   | cpp        | CWE-287   |             328 |                   12 |
| Big-Vul   | cpp        | CWE-369   |             275 |                   10 |
| Big-Vul   | cpp        | CWE-400   |             324 |                    9 |
| Big-Vul   | cpp        | CWE-94    |             152 |                    9 |
| Big-Vul   | cpp        | CWE-78    |             199 |                    8 |
| Big-Vul   | cpp        | CWE-617   |             723 |                    7 |
| Big-Vul   | cpp        | CWE-354   |              21 |                    7 |
| Big-Vul   | cpp        | CWE-18    |              20 |                    7 |
| Big-Vul   | cpp        | CWE-754   |             233 |                    6 |
| Big-Vul   | cpp        | CWE-320   |             110 |                    6 |
| Big-Vul   | cpp        | CWE-255   |              62 |                    6 |
| Big-Vul   | cpp        | CWE-281   |              39 |                    6 |
| Big-Vul   | cpp        | CWE-611   |             239 |                    5 |
| Big-Vul   | cpp        | CWE-120   |              45 |                    5 |
| Big-Vul   | cpp        | CWE-674   |              30 |                    5 |
| Big-Vul   | cpp        | CWE-388   |              93 |                    4 |
| Big-Vul   | cpp        | CWE-436   |              72 |                    4 |
| Big-Vul   | cpp        | CWE-770   |              36 |                    4 |
| Big-Vul   | cpp        | CWE-346   |              59 |                    3 |
| Big-Vul   | cpp        | CWE-295   |              57 |                    3 |
| Big-Vul   | cpp        | CWE-347   |              21 |                    3 |
| Big-Vul   | cpp        | CWE-77    |             100 |                    2 |
| Big-Vul   | cpp        | CWE-862   |              41 |                    2 |
| Big-Vul   | cpp        | CWE-601   |              37 |                    2 |
| Big-Vul   | cpp        | CWE-426   |              22 |                    2 |
| Big-Vul   | cpp        | CWE-522   |               6 |                    2 |
| Big-Vul   | cpp        | CWE-327   |               3 |                    2 |
| Big-Vul   | cpp        | CWE-682   |               3 |                    2 |
| Big-Vul   | cpp        | CWE-345   |               2 |                    2 |
| Big-Vul   | cpp        | CWE-532   |              67 |                    1 |
| Big-Vul   | cpp        | CWE-330   |              50 |                    1 |
| Big-Vul   | cpp        | CWE-1021  |              43 |                    1 |
| Big-Vul   | cpp        | CWE-834   |              33 |                    1 |
| Big-Vul   | cpp        | CWE-352   |              29 |                    1 |
| Big-Vul   | cpp        | CWE-502   |              21 |                    1 |
| Big-Vul   | cpp        | CWE-90    |              17 |                    1 |
| Big-Vul   | cpp        | CWE-755   |              14 |                    1 |
| Big-Vul   | cpp        | CWE-664   |              13 |                    1 |
| Big-Vul   | cpp        | CWE-74    |               9 |                    1 |
| Big-Vul   | cpp        | CWE-824   |               6 |                    1 |
| Big-Vul   | cpp        | CWE-209   |               1 |                    1 |
| Big-Vul   | cpp        | CWE-252   |               1 |                    1 |
| Big-Vul   | cpp        | CWE-93    |              91 |                    0 |
| Big-Vul   | cpp        | CWE-290   |              58 |                    0 |
| Big-Vul   | cpp        | CWE-89    |              47 |                    0 |
| Big-Vul   | cpp        | CWE-16    |              23 |                    0 |
| Big-Vul   | cpp        | CWE-668   |              20 |                    0 |
| Big-Vul   | cpp        | CWE-918   |              14 |                    0 |
| Big-Vul   | cpp        | CWE-706   |              12 |                    0 |
| Big-Vul   | cpp        | CWE-693   |              11 |                    0 |
| Big-Vul   | cpp        | CWE-191   |               7 |                    0 |
| Big-Vul   | cpp        | CWE-665   |               3 |                    0 |
| Big-Vul   | cpp        | CWE-769   |               3 |                    0 |
| Big-Vul   | cpp        | CWE-129   |               2 |                    0 |
| Big-Vul   | cpp        | CWE-172   |               2 |                    0 |
| Big-Vul   | cpp        | CWE-361   |               2 |                    0 |
| Big-Vul   | cpp        | CWE-494   |               2 |                    0 |
| Big-Vul   | cpp        | CWE-909   |               2 |                    0 |

## 4. Label Noise Findings

Conflicting groups are groups where the same selected hash has more than one distinct label. They require manual review; a conflict alone does not prove that a label is wrong.

| Dataset | Conflict groups | Random groups exported | Review CSV |
|---|---:|---:|---|
| MegaVul | 0 | 0 | `None` |
| Big-Vul | 0 | 0 | `None` |

**Manual review status:** NOT COMPLETED BY THIS SCRIPT.

Open each review CSV, inspect the code, label, CWE, and source context, then record the manually confirmed findings here. Do not treat the number of conflicting groups as the number of confirmed label errors.

## 5. Cross-Dataset Overlap

| dataset_a   | dataset_b   |   unique_hashes_a |   unique_hashes_b |   shared_hashes |   overlap_pct_a |   overlap_pct_b |
|:------------|:------------|------------------:|------------------:|----------------:|----------------:|----------------:|
| MegaVul     | Big-Vul     |            336896 |            103349 |               0 |               0 |               0 |

Overlap is based on the selected hash column when present; otherwise, it is based on SHA-256 using the language-specific normalizers from the deduplication pipeline. For the final deduped files, zero shared hashes is expected because cross-dataset duplicates were removed during deduplication.

## 6. Recommended CWE List per Language

The table below ranks CWE groups by vulnerable sample count. It is a candidate list, not an automatic acceptance decision. Apply the project's official D22 threshold and verify the label convention before selecting CWE groups for downstream experiments.

| dataset   | language   | cwe      |   total_samples |   vulnerable_samples |   rank_within_dataset_language |
|:----------|:-----------|:---------|----------------:|---------------------:|-------------------------------:|
| MegaVul   | cpp        | CWE-119  |           26407 |                 1591 |                              1 |
| MegaVul   | cpp        | CWE-787  |           28139 |                 1518 |                              2 |
| MegaVul   | cpp        | CWE-125  |           23588 |                 1453 |                              3 |
| MegaVul   | cpp        | CWE-476  |           26969 |                 1290 |                              4 |
| MegaVul   | cpp        | CWE-20   |           19452 |                 1074 |                              5 |
| Big-Vul   | cpp        | CWE-119  |           13556 |                 1064 |                              6 |
| MegaVul   | cpp        | CWE-416  |           24602 |                 1007 |                              7 |
| MegaVul   | cpp        | CWE-190  |           11789 |                  711 |                              8 |
| Big-Vul   | cpp        | CWE-20   |           12631 |                  617 |                              9 |
| MegaVul   | cpp        | CWE-200  |           11802 |                  561 |                             10 |
| MegaVul   | cpp        | CWE-362  |           10623 |                  509 |                             11 |
| Big-Vul   | cpp        | CWE-399  |            8627 |                  481 |                             12 |
| MegaVul   | cpp        | CWE-399  |            9986 |                  440 |                             13 |
| MegaVul   | cpp        | CWE-264  |            9541 |                  426 |                             14 |
| MegaVul   | cpp        | CWE-120  |            6658 |                  424 |                             15 |
| MegaVul   | cpp        | CWE-400  |            6223 |                  313 |                             16 |
| MegaVul   | cpp        | CWE-189  |            6006 |                  296 |                             17 |
| MegaVul   | cpp        | CWE-401  |           11501 |                  280 |                             18 |
| Big-Vul   | cpp        | CWE-125  |            3256 |                  263 |                             19 |
| MegaVul   | cpp        | CWE-617  |            4040 |                  261 |                             20 |
| MegaVul   | cpp        | CWE-835  |            5081 |                  252 |                             21 |
| Big-Vul   | cpp        | CWE-200  |            3835 |                  233 |                             22 |
| Big-Vul   | cpp        | CWE-264  |            5463 |                  203 |                             23 |
| MegaVul   | cpp        | CWE-415  |            6091 |                  184 |                             24 |
| MegaVul   | cpp        | CWE-369  |            2510 |                  178 |                             25 |
| Big-Vul   | cpp        | CWE-416  |            5717 |                  178 |                             26 |
| MegaVul   | cpp        | CWE-772  |            2974 |                  174 |                             27 |
| Big-Vul   | cpp        | CWE-189  |            3128 |                  168 |                             28 |
| MegaVul   | cpp        | CWE-22   |            3760 |                  157 |                             29 |
| Big-Vul   | cpp        | CWE-362  |            2593 |                  142 |                             30 |
| Big-Vul   | cpp        | CWE-190  |            1921 |                  136 |                             31 |
| MegaVul   | cpp        | CWE-254  |            2872 |                  128 |                             32 |
| MegaVul   | cpp        | CWE-674  |            1985 |                  123 |                             33 |
| MegaVul   | cpp        | CWE-122  |            2090 |                  115 |                             34 |
| MegaVul   | cpp        | CWE-908  |            1817 |                  103 |                             35 |
| Big-Vul   | cpp        | CWE-787  |            1592 |                  101 |                             36 |
| MegaVul   | cpp        | CWE-59   |            1747 |                   95 |                             37 |
| Big-Vul   | cpp        | CWE-284  |            1279 |                   95 |                             38 |
| MegaVul   | cpp        | CWE-770  |            2022 |                   94 |                             39 |
| MegaVul   | cpp        | CWE-287  |            1626 |                   94 |                             40 |
| MegaVul   | cpp        | CWE-284  |            1452 |                   93 |                             41 |
| MegaVul   | cpp        | CWE-834  |            4158 |                   88 |                             42 |
| MegaVul   | cpp        | CWE-310  |            1302 |                   80 |                             43 |
| MegaVul   | cpp        | CWE-909  |            1327 |                   78 |                             44 |
| Big-Vul   | cpp        | CWE-254  |            2094 |                   78 |                             45 |
| MegaVul   | cpp        | CWE-74   |            2384 |                   73 |                             46 |
| MegaVul   | cpp        | CWE-295  |            1944 |                   71 |                             47 |
| MegaVul   | cpp        | CWE-269  |            1013 |                   70 |                             48 |
| MegaVul   | cpp        | CWE-667  |            1421 |                   69 |                             49 |
| MegaVul   | cpp        | CWE-17   |            1002 |                   65 |                             50 |
| MegaVul   | cpp        | CWE-193  |             889 |                   64 |                             51 |
| MegaVul   | cpp        | CWE-78   |            1296 |                   60 |                             52 |
| MegaVul   | cpp        | CWE-459  |             660 |                   60 |                             53 |
| MegaVul   | cpp        | CWE-404  |            1748 |                   59 |                             54 |
| MegaVul   | cpp        | CWE-843  |            1094 |                   59 |                             55 |
| MegaVul   | cpp        | CWE-754  |             930 |                   58 |                             56 |
| MegaVul   | cpp        | CWE-79   |             914 |                   58 |                             57 |
| MegaVul   | cpp        | CWE-732  |             829 |                   58 |                             58 |
| Big-Vul   | cpp        | CWE-476  |            1891 |                   57 |                             59 |
| MegaVul   | cpp        | CWE-19   |            1271 |                   55 |                             60 |
| MegaVul   | cpp        | CWE-681  |             704 |                   52 |                             61 |
| MegaVul   | cpp        | CWE-863  |            1229 |                   49 |                             62 |
| MegaVul   | cpp        | CWE-755  |            1048 |                   42 |                             63 |
| MegaVul   | cpp        | CWE-252  |             526 |                   42 |                             64 |
| Big-Vul   | cpp        | CWE-415  |             321 |                   42 |                             65 |
| MegaVul   | cpp        | CWE-665  |            1032 |                   40 |                             66 |
| Big-Vul   | cpp        | CWE-310  |             602 |                   40 |                             67 |
| Big-Vul   | cpp        | CWE-732  |            1119 |                   38 |                             68 |
| MegaVul   | cpp        | CWE-89   |            1743 |                   37 |                             69 |
| Big-Vul   | cpp        | CWE-19   |             363 |                   37 |                             70 |
| MegaVul   | cpp        | CWE-668  |             853 |                   35 |                             71 |
| MegaVul   | cpp        | CWE-129  |             726 |                   34 |                             72 |
| Big-Vul   | cpp        | CWE-404  |             700 |                   34 |                             73 |
| MegaVul   | cpp        | CWE-203  |             737 |                   33 |                             74 |
| MegaVul   | cpp        | CWE-367  |             952 |                   32 |                             75 |
| MegaVul   | cpp        | CWE-704  |             748 |                   32 |                             76 |
| MegaVul   | cpp        | CWE-682  |             581 |                   32 |                             77 |
| MegaVul   | cpp        | CWE-131  |             528 |                   32 |                             78 |
| MegaVul   | cpp        | CWE-1284 |             368 |                   32 |                             79 |
| Big-Vul   | cpp        | CWE-79   |             545 |                   32 |                             80 |
| MegaVul   | cpp        | CWE-330  |             504 |                   31 |                             81 |
| MegaVul   | cpp        | CWE-862  |             459 |                   30 |                             82 |
| MegaVul   | cpp        | CWE-354  |             445 |                   30 |                             83 |
| MegaVul   | cpp        | CWE-763  |             439 |                   30 |                             84 |
| MegaVul   | cpp        | CWE-134  |            1055 |                   28 |                             85 |
| MegaVul   | cpp        | CWE-191  |             817 |                   27 |                             86 |
| MegaVul   | cpp        | CWE-824  |             507 |                   25 |                             87 |
| MegaVul   | cpp        | CWE-327  |             314 |                   25 |                             88 |
| Big-Vul   | cpp        | CWE-22   |             479 |                   25 |                             89 |
| MegaVul   | cpp        | CWE-276  |             674 |                   24 |                             90 |
| MegaVul   | cpp        | CWE-77   |             418 |                   24 |                             91 |
| MegaVul   | cpp        | CWE-121  |             233 |                   23 |                             92 |
| MegaVul   | cpp        | CWE-502  |             113 |                   22 |                             93 |
| Big-Vul   | cpp        | CWE-59   |             547 |                   22 |                             94 |
| Big-Vul   | cpp        | CWE-285  |             369 |                   22 |                             95 |
| MegaVul   | cpp        | CWE-212  |             291 |                   21 |                             96 |
| MegaVul   | cpp        | CWE-697  |             239 |                   21 |                             97 |
| Big-Vul   | cpp        | CWE-772  |             177 |                   21 |                             98 |
| MegaVul   | cpp        | CWE-345  |             196 |                   20 |                             99 |
| MegaVul   | cpp        | CWE-94   |             396 |                   19 |                            100 |
| MegaVul   | cpp        | CWE-436  |             281 |                   19 |                            101 |
| Big-Vul   | cpp        | CWE-835  |             440 |                   19 |                            102 |
| MegaVul   | cpp        | CWE-611  |             240 |                   18 |                            103 |
| MegaVul   | cpp        | CWE-444  |             186 |                   18 |                            104 |
| MegaVul   | cpp        | CWE-326  |             157 |                   18 |                            105 |
| MegaVul   | cpp        | CWE-662  |             111 |                   18 |                            106 |
| MegaVul   | cpp        | CWE-776  |              81 |                   18 |                            107 |
| Big-Vul   | cpp        | CWE-269  |             277 |                   18 |                            108 |
| MegaVul   | cpp        | CWE-434  |             574 |                   16 |                            109 |
| Big-Vul   | cpp        | CWE-134  |             547 |                   16 |                            110 |
| Big-Vul   | cpp        | CWE-17   |             275 |                   16 |                            111 |
| Big-Vul   | cpp        | CWE-311  |             164 |                   16 |                            112 |
| MegaVul   | cpp        | CWE-116  |             455 |                   15 |                            113 |
| MegaVul   | cpp        | CWE-601  |             216 |                   15 |                            114 |
| Big-Vul   | cpp        | CWE-358  |              48 |                   14 |                            115 |
| MegaVul   | cpp        | CWE-672  |              81 |                   13 |                            116 |
| Big-Vul   | cpp        | CWE-704  |             475 |                   13 |                            117 |
| MegaVul   | cpp        | CWE-347  |             101 |                   12 |                            118 |
| Big-Vul   | cpp        | CWE-287  |             328 |                   12 |                            119 |
| MegaVul   | cpp        | CWE-440  |             636 |                   11 |                            120 |
| MegaVul   | cpp        | CWE-426  |             201 |                   10 |                            121 |
| MegaVul   | cpp        | CWE-613  |              44 |                   10 |                            122 |
| MegaVul   | cpp        | CWE-197  |              35 |                   10 |                            123 |
| Big-Vul   | cpp        | CWE-369  |             275 |                   10 |                            124 |
| MegaVul   | cpp        | CWE-552  |             338 |                    9 |                            125 |
| MegaVul   | cpp        | CWE-384  |             217 |                    9 |                            126 |
| MegaVul   | cpp        | CWE-319  |             166 |                    9 |                            127 |
| MegaVul   | cpp        | CWE-306  |             113 |                    9 |                            128 |
| Big-Vul   | cpp        | CWE-400  |             324 |                    9 |                            129 |
| Big-Vul   | cpp        | CWE-94   |             152 |                    9 |                            130 |
| MegaVul   | cpp        | CWE-1021 |             501 |                    8 |                            131 |
| MegaVul   | cpp        | CWE-346  |             232 |                    8 |                            132 |
| MegaVul   | cpp        | CWE-670  |             170 |                    8 |                            133 |
| MegaVul   | cpp        | CWE-388  |             123 |                    8 |                            134 |
| MegaVul   | cpp        | CWE-918  |             103 |                    8 |                            135 |
| MegaVul   | cpp        | CWE-290  |              79 |                    8 |                            136 |
| MegaVul   | cpp        | CWE-913  |              46 |                    8 |                            137 |
| Big-Vul   | cpp        | CWE-78   |             199 |                    8 |                            138 |
| MegaVul   | cpp        | CWE-428  |             106 |                    7 |                            139 |
| MegaVul   | cpp        | CWE-911  |             102 |                    7 |                            140 |
| Big-Vul   | cpp        | CWE-617  |             723 |                    7 |                            141 |
| Big-Vul   | cpp        | CWE-354  |              21 |                    7 |                            142 |
| Big-Vul   | cpp        | CWE-18   |              20 |                    7 |                            143 |
| MegaVul   | cpp        | CWE-532  |             127 |                    6 |                            144 |
| MegaVul   | cpp        | CWE-90   |              91 |                    6 |                            145 |
| MegaVul   | cpp        | CWE-407  |              59 |                    6 |                            146 |
| MegaVul   | cpp        | CWE-331  |              38 |                    6 |                            147 |
| MegaVul   | cpp        | CWE-18   |              36 |                    6 |                            148 |
| MegaVul   | cpp        | CWE-385  |              18 |                    6 |                            149 |
| Big-Vul   | cpp        | CWE-754  |             233 |                    6 |                            150 |
| Big-Vul   | cpp        | CWE-320  |             110 |                    6 |                            151 |
| Big-Vul   | cpp        | CWE-255  |              62 |                    6 |                            152 |
| Big-Vul   | cpp        | CWE-281  |              39 |                    6 |                            153 |
| MegaVul   | cpp        | CWE-693  |             328 |                    5 |                            154 |
| MegaVul   | cpp        | CWE-680  |             143 |                    5 |                            155 |
| MegaVul   | cpp        | CWE-823  |             114 |                    5 |                            156 |
| MegaVul   | cpp        | CWE-1187 |              78 |                    5 |                            157 |
| MegaVul   | cpp        | CWE-126  |              26 |                    5 |                            158 |
| MegaVul   | cpp        | CWE-337  |              21 |                    5 |                            159 |
| MegaVul   | cpp        | CWE-409  |              17 |                    5 |                            160 |
| Big-Vul   | cpp        | CWE-611  |             239 |                    5 |                            161 |
| Big-Vul   | cpp        | CWE-120  |              45 |                    5 |                            162 |
| Big-Vul   | cpp        | CWE-674  |              30 |                    5 |                            163 |
| MegaVul   | cpp        | CWE-427  |             360 |                    4 |                            164 |
| MegaVul   | cpp        | CWE-16   |             309 |                    4 |                            165 |
| MegaVul   | cpp        | CWE-285  |             191 |                    4 |                            166 |
| MegaVul   | cpp        | CWE-273  |             161 |                    4 |                            167 |
| MegaVul   | cpp        | CWE-1077 |             100 |                    4 |                            168 |
| MegaVul   | cpp        | CWE-522  |              67 |                    4 |                            169 |
| MegaVul   | cpp        | CWE-626  |              55 |                    4 |                            170 |
| MegaVul   | cpp        | CWE-88   |              28 |                    4 |                            171 |
| MegaVul   | cpp        | CWE-338  |              22 |                    4 |                            172 |
| MegaVul   | cpp        | CWE-241  |              21 |                    4 |                            173 |
| Big-Vul   | cpp        | CWE-388  |              93 |                    4 |                            174 |
| Big-Vul   | cpp        | CWE-436  |              72 |                    4 |                            175 |
| Big-Vul   | cpp        | CWE-770  |              36 |                    4 |                            176 |
| MegaVul   | cpp        | CWE-1188 |             260 |                    3 |                            177 |
| MegaVul   | cpp        | CWE-706  |             146 |                    3 |                            178 |
| MegaVul   | cpp        | CWE-229  |             113 |                    3 |                            179 |
| MegaVul   | cpp        | CWE-494  |              48 |                    3 |                            180 |
| MegaVul   | cpp        | CWE-325  |              39 |                    3 |                            181 |
| MegaVul   | cpp        | CWE-118  |              32 |                    3 |                            182 |
| MegaVul   | cpp        | CWE-172  |              17 |                    3 |                            183 |
| MegaVul   | cpp        | CWE-707  |              16 |                    3 |                            184 |
| Big-Vul   | cpp        | CWE-346  |              59 |                    3 |                            185 |
| Big-Vul   | cpp        | CWE-295  |              57 |                    3 |                            186 |
| Big-Vul   | cpp        | CWE-347  |              21 |                    3 |                            187 |
| MegaVul   | cpp        | CWE-639  |             116 |                    2 |                            188 |
| MegaVul   | cpp        | CWE-307  |              34 |                    2 |                            189 |
| MegaVul   | cpp        | CWE-838  |              34 |                    2 |                            190 |
| MegaVul   | cpp        | CWE-320  |              23 |                    2 |                            191 |
| MegaVul   | cpp        | CWE-113  |              17 |                    2 |                            192 |
| MegaVul   | cpp        | CWE-924  |              12 |                    2 |                            193 |
| MegaVul   | cpp        | CWE-255  |               8 |                    2 |                            194 |
| MegaVul   | cpp        | CWE-762  |               7 |                    2 |                            195 |
| MegaVul   | cpp        | CWE-1333 |               3 |                    2 |                            196 |
| Big-Vul   | cpp        | CWE-77   |             100 |                    2 |                            197 |
| Big-Vul   | cpp        | CWE-862  |              41 |                    2 |                            198 |
| Big-Vul   | cpp        | CWE-601  |              37 |                    2 |                            199 |
| Big-Vul   | cpp        | CWE-426  |              22 |                    2 |                            200 |
| Big-Vul   | cpp        | CWE-522  |               6 |                    2 |                            201 |
| Big-Vul   | cpp        | CWE-327  |               3 |                    2 |                            202 |
| Big-Vul   | cpp        | CWE-682  |               3 |                    2 |                            203 |
| Big-Vul   | cpp        | CWE-345  |               2 |                    2 |                            204 |
| MegaVul   | cpp        | CWE-250  |             587 |                    1 |                            205 |
| MegaVul   | cpp        | CWE-312  |             187 |                    1 |                            206 |
| MegaVul   | cpp        | CWE-460  |              89 |                    1 |                            207 |
| MegaVul   | cpp        | CWE-1050 |              75 |                    1 |                            208 |
| MegaVul   | cpp        | CWE-358  |              66 |                    1 |                            209 |
| MegaVul   | cpp        | CWE-248  |              60 |                    1 |                            210 |
| MegaVul   | cpp        | CWE-349  |              60 |                    1 |                            211 |
| MegaVul   | cpp        | CWE-300  |              56 |                    1 |                            212 |
| MegaVul   | cpp        | CWE-943  |              56 |                    1 |                            213 |
| MegaVul   | cpp        | CWE-93   |              47 |                    1 |                            214 |
| MegaVul   | cpp        | CWE-282  |              31 |                    1 |                            215 |
| MegaVul   | cpp        | CWE-23   |              27 |                    1 |                            216 |
| MegaVul   | cpp        | CWE-26   |              27 |                    1 |                            217 |
| MegaVul   | cpp        | CWE-361  |              27 |                    1 |                            218 |
| MegaVul   | cpp        | CWE-788  |              23 |                    1 |                            219 |
| MegaVul   | cpp        | CWE-335  |              22 |                    1 |                            220 |
| MegaVul   | cpp        | CWE-590  |              22 |                    1 |                            221 |
| MegaVul   | cpp        | CWE-475  |              21 |                    1 |                            222 |
| MegaVul   | cpp        | CWE-352  |              17 |                    1 |                            223 |
| MegaVul   | cpp        | CWE-628  |              15 |                    1 |                            224 |
| MegaVul   | cpp        | CWE-323  |              12 |                    1 |                            225 |
| MegaVul   | cpp        | CWE-73   |              11 |                    1 |                            226 |
| MegaVul   | cpp        | CWE-117  |               9 |                    1 |                            227 |
| MegaVul   | cpp        | CWE-185  |               8 |                    1 |                            228 |
| MegaVul   | cpp        | CWE-1049 |               7 |                    1 |                            229 |
| MegaVul   | cpp        | CWE-610  |               7 |                    1 |                            230 |
| MegaVul   | cpp        | CWE-202  |               3 |                    1 |                            231 |
| MegaVul   | cpp        | CWE-324  |               2 |                    1 |                            232 |
| MegaVul   | cpp        | CWE-209  |               1 |                    1 |                            233 |
| Big-Vul   | cpp        | CWE-532  |              67 |                    1 |                            234 |
| Big-Vul   | cpp        | CWE-330  |              50 |                    1 |                            235 |
| Big-Vul   | cpp        | CWE-1021 |              43 |                    1 |                            236 |
| Big-Vul   | cpp        | CWE-834  |              33 |                    1 |                            237 |
| Big-Vul   | cpp        | CWE-352  |              29 |                    1 |                            238 |
| Big-Vul   | cpp        | CWE-502  |              21 |                    1 |                            239 |
| Big-Vul   | cpp        | CWE-90   |              17 |                    1 |                            240 |
| Big-Vul   | cpp        | CWE-755  |              14 |                    1 |                            241 |
| Big-Vul   | cpp        | CWE-664  |              13 |                    1 |                            242 |
| Big-Vul   | cpp        | CWE-74   |               9 |                    1 |                            243 |
| Big-Vul   | cpp        | CWE-824  |               6 |                    1 |                            244 |
| Big-Vul   | cpp        | CWE-209  |               1 |                    1 |                            245 |
| Big-Vul   | cpp        | CWE-252  |               1 |                    1 |                            246 |
| MegaVul   | cpp        | CWE-208  |               5 |                    0 |                            247 |
| Big-Vul   | cpp        | CWE-93   |              91 |                    0 |                            248 |
| Big-Vul   | cpp        | CWE-290  |              58 |                    0 |                            249 |
| Big-Vul   | cpp        | CWE-89   |              47 |                    0 |                            250 |
| Big-Vul   | cpp        | CWE-16   |              23 |                    0 |                            251 |
| Big-Vul   | cpp        | CWE-668  |              20 |                    0 |                            252 |
| Big-Vul   | cpp        | CWE-918  |              14 |                    0 |                            253 |
| Big-Vul   | cpp        | CWE-706  |              12 |                    0 |                            254 |
| Big-Vul   | cpp        | CWE-693  |              11 |                    0 |                            255 |
| Big-Vul   | cpp        | CWE-191  |               7 |                    0 |                            256 |
| Big-Vul   | cpp        | CWE-665  |               3 |                    0 |                            257 |
| Big-Vul   | cpp        | CWE-769  |               3 |                    0 |                            258 |
| Big-Vul   | cpp        | CWE-129  |               2 |                    0 |                            259 |
| Big-Vul   | cpp        | CWE-172  |               2 |                    0 |                            260 |
| Big-Vul   | cpp        | CWE-361  |               2 |                    0 |                            261 |
| Big-Vul   | cpp        | CWE-494  |               2 |                    0 |                            262 |
| Big-Vul   | cpp        | CWE-909  |               2 |                    0 |                            263 |

## 7. Acceptance Verdict

| Dataset | Verdict | Reason |
|---|---|---|
| MegaVul | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |
| Big-Vul | PRELIMINARY PASS | basic automated checks passed; official D22 thresholds and manual label-noise review still need confirmation |

### Scope and Limitations

- Only MegaVul and Big-Vul were audited.
- This report does not provide a verdict for the other two project datasets.
- Manual label-noise review is still required.
- Official D22 acceptance thresholds must be checked against project docs.
- If the dedupe pipeline used a different normalization/hash algorithm, the overlap and duplicate-hash results must be recomputed using that exact method.
