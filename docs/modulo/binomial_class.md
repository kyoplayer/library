---
title: 素数$mod$二項係数(class ver.)
documentation_of: //library/modulo/binomial_class.py
---

## 説明

このファイルでは、`CombinationClass`クラスを提供する。

このクラスには次の関数が定義されている。

- `__init__(self, max_n:int, mod:int) -> None`

$0$から$n$までの長さ$n+1$の階乗、逆階乗テーブルを作成する。
$O(n+\log mod)$

- `calc_comb(self, n:int, k:int) -> int`

$\displaystyle \binom{n}{k} \pmod {mod}$を求める。$n < k$なら$0$を返す。$O(1)$