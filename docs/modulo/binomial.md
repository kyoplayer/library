---
title: 素数$mod$二項係数
documentation_of: //library/modulo/binomial.py
---

## 説明

このファイルでは、以下の$3$つの関数を提供する。

- `init(n:int, mod:int) -> None`

$0$から$n$までの長さ$n+1$の階乗、逆階乗テーブルを作成し、グローバル領域に保存する。
$O(n+\log mod)$

- `calc_comb(n:int, k:int, mod:int) -> int`

$\displaystyle \binom{n}{k} \pmod {mod}$を求める。$n < k$なら$0$を返す。$O(1)$

- `calc_comb_998244353(n:int, k:int) -> int`

$\displaystyle \binom{n}{k} \pmod {998244353}$を求める。$n < k$なら$0$を返す。$O(1)$