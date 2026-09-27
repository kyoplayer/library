---
title: 階乗, 逆階乗, その両方(make tables)
documentation_of: //library/math/factorial.py
---

## 説明
このファイルでは、$3$つの基本関数を提供する。

- `make_factorial_table(max_n:int, mod:int) -> list[int]`

$[0!,1!,2!,3!,\dots, max_n!]$を返す関数。ただし、各要素は素数modで割ったあまりをとる。
$O(max_n)$

- `make_invFactorial_table(max_n:int, mod:int) -> list[int]`

$\displaystyle [{0!}^{-1},{1!}^{-1},{2!}^{-1},\dots, {max_n !}^{-1}]$を返す関数。ただし、各要素は素数$mod$を法とした逆元を表す。
$O(max_n)$

- `make_factorial_and_invFactorial_table(max_n:int,mod:int) -> tuple[list[int],list[int]]`

階乗と逆階乗の両方のテーブルをこの順に返す関数。$max_n < mod$を要求する(そうでないと誤動作する)。上の$2$つの関数で別々に作るより定数倍がいい。
$O(max_n + \log mod)$