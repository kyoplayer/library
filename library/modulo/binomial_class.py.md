---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/math/factorial.py
    title: "\u968E\u4E57, \u9006\u968E\u4E57, \u305D\u306E\u4E21\u65B9(make tables)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: verify/yosupo_modulo/modulo_binomial_class.test.codon
    title: verify/yosupo_modulo/modulo_binomial_class.test.codon
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes: {}
  bundledCode: "def make_factorial_table(max_n:int,mod:int) -> list[int]:\n    \"\"\
    \"\u4EFB\u610F\u7D20\u6570\u306B\u5BFE\u3057\u3066max_n\u307E\u3067\u306E\u968E\
    \u4E57\u306E\u30C6\u30FC\u30D6\u30EB\u3092\u4F5C\u6210\u3059\u308B\u95A2\u6570\
    , O(max_n)\"\"\"\n    fact : list[int] = [0]*(max_n+1)\n    fact[0] = fact[1]\
    \ = 1 #0! = 1\n    for i in range(2,max_n+1):\n        fact[i] = (fact[i-1] *\
    \ i) % mod\n    return fact\n\ndef make_invFactorial_table(max_n:int,mod:int)\
    \ -> list[int]:\n    \"\"\"\u4EFB\u610F\u7D20\u6570\u306B\u5BFE\u3057\u3066max_n\u307E\
    \u3067\u306E\u9006\u968E\u4E57\u306E\u30C6\u30FC\u30D6\u30EB\u3092\u4F5C\u6210\
    \u3059\u308B\u95A2\u6570, O(max_n)\"\"\"\n    inv : list[int] = [0]*(max_n+1)\n\
    \    fact_inv : list[int] = [0]*(max_n+1)\n    inv[1] = 1\n    fact_inv[0] = fact_inv[1]\
    \ = 1\n    for i in range(2,max_n+1):\n        inv[i] = mod - inv[mod % i] * (mod//i)\
    \ % mod\n        fact_inv[i] = (fact_inv[i-1] * inv[i]) % mod\n    return fact_inv\n\
    \ndef make_factorial_and_invFactorial_table(max_n:int,mod:int) -> tuple[list[int],list[int]]:\n\
    \    \"\"\"\u4EFB\u610F\u7D20\u6570\u306B\u5BFE\u3057\u3066max_n\u307E\u3067\u306E\
    \u968E\u4E57\u30FB\u9006\u968E\u4E57\u306E\u30C6\u30FC\u30D6\u30EB\u3092\u4F5C\
    \u6210\u3059\u308B\u95A2\u6570, \u5225\u3005\u306B\u4F5C\u308B\u3088\u308A\u52B9\
    \u7387\u304C\u3044\u3044\u3002\n    max_n < mod \u3092\u4EEE\u5B9A\u3059\u308B\
    \u3002\n    O(max_n + log mod)\"\"\"\n    fact : list[int] = [0]*(max_n+1)\n \
    \   fact_inv : list[int] = [0]*(max_n+1)\n    fact[0] = fact[1] = 1\n    fact_inv[0]\
    \ = fact_inv[1] = 1\n    for i in range(2,max_n+1):\n        fact[i] = (fact[i-1]*i)\
    \ % mod\n    fact_inv[max_n] = pow(fact[max_n],mod-2,mod)\n\n    for i in range(max_n,1,-1):\n\
    \        fact_inv[i-1] = (fact_inv[i]*i) % mod\n\n    return (fact,fact_inv)\n\
    \nclass CombinationClass:\n    fact : list[int]; inv_fact : list[int]; max_n :\
    \ int; mod : int\n    def __init__(self,max_n:int,mod:int) -> None:\n        self.max_n\
    \ = max_n\n        self.mod = mod\n        self.fact = []\n        self.inv_fact\
    \ = []\n        self.fact,self.inv_fact = make_factorial_and_invFactorial_table(max_n,mod)\n\
    \        pass\n\n    def calc_comb(self,n:int,k:int) -> int:\n        \"\"\"\u4E8C\
    \u9805\u4FC2\u6570nCk\u3092__init__\u3067\u5B9A\u7FA9\u3055\u308C\u305Fmod\u3067\
    O(1)\u3067\u6C42\u3081\u308B\u95A2\u6570\"\"\"\n        if n < k:\n          \
    \  return 0\n        return ((self.fact[n] * self.inv_fact[k]) % self.mod * self.inv_fact[n-k])\
    \ % self.mod\n"
  code: "from ...library.math.factorial import make_factorial_and_invFactorial_table\n\
    \nclass CombinationClass:\n    fact : list[int]; inv_fact : list[int]; max_n :\
    \ int; mod : int\n    def __init__(self,max_n:int,mod:int) -> None:\n        self.max_n\
    \ = max_n\n        self.mod = mod\n        self.fact = []\n        self.inv_fact\
    \ = []\n        self.fact,self.inv_fact = make_factorial_and_invFactorial_table(max_n,mod)\n\
    \        pass\n\n    def calc_comb(self,n:int,k:int) -> int:\n        \"\"\"\u4E8C\
    \u9805\u4FC2\u6570nCk\u3092__init__\u3067\u5B9A\u7FA9\u3055\u308C\u305Fmod\u3067\
    O(1)\u3067\u6C42\u3081\u308B\u95A2\u6570\"\"\"\n        if n < k:\n          \
    \  return 0\n        return ((self.fact[n] * self.inv_fact[k]) % self.mod * self.inv_fact[n-k])\
    \ % self.mod"
  dependsOn:
  - library/math/factorial.py
  isVerificationFile: false
  path: library/modulo/binomial_class.py
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - verify/yosupo_modulo/modulo_binomial_class.test.codon
documentation_of: library/modulo/binomial_class.py
layout: document
title: "\u7D20\u6570$mod$\u4E8C\u9805\u4FC2\u6570(class ver.)"
---

## 説明

このファイルでは、`CombinationClass`クラスを提供する。

このクラスには次の関数が定義されている。

- `__init__(self, max_n:int, mod:int) -> None`

$0$から$n$までの長さ$n+1$の階乗、逆階乗テーブルを作成する。
$O(n+\log mod)$

- `calc_comb(self, n:int, k:int) -> int`

$\displaystyle \binom{n}{k} \pmod {mod}$を求める。$n < k$なら$0$を返す。$O(1)$