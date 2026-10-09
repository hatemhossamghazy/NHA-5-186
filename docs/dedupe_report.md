# Dedupe v0 report

| dataset | original | language-filtered | empty | label conflicts | internal dups | cross dups | final |
| --- | --- | --- | --- | --- | --- | --- | --- |
| megavul | 353,858 | 0 | 0 | 1,310 | 15,745 | 0 | 336,803 |
| bigvul | 217,007 | 0 | 0 | 3,042 | 52,300 | 58,320 | 103,345 |
| cvefixes_cpp | 15,222 | 11,405 | 0 | 239 | 41 | 909 | 2,628 |
| cvefixes_python | 4,943 | 0 | 0 | 412 | 34 | 11 | 4,486 |

## Language values removed by the language filter

- cvefixes_cpp: {'c': 11405}

Conflicting hash groups (same code, different label): 1,834

## Overlap between datasets (shared normalized hashes)

| dataset A | dataset B | shared |
| --- | --- | --- |
| megavul | bigvul | 58,320 |
| megavul | cvefixes_cpp | 853 |
| megavul | cvefixes_python | 1 |
| bigvul | cvefixes_cpp | 106 |
| bigvul | cvefixes_python | 0 |
| cvefixes_cpp | cvefixes_python | 10 |
