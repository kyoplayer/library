---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/modulo/binomial_class.py
    title: "\u7D20\u6570$mod$\u4E8C\u9805\u4FC2\u6570(class ver.)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: codon
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
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
    \ % self.mod\n# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    \n\nTT,mod = list(map(int,input().split()))\nC = CombinationClass(min(10**7,mod)-1,mod)\n\
    \nfor _ in range(TT):\n    n,k = list(map(int,input().split()))\n    res = C.calc_comb(n,k)\n\
    \    print(res)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    \nfrom ...library.modulo.binomial_class import CombinationClass\n\nTT,mod = list(map(int,input().split()))\n\
    C = CombinationClass(min(10**7,mod)-1,mod)\n\nfor _ in range(TT):\n    n,k = list(map(int,input().split()))\n\
    \    res = C.calc_comb(n,k)\n    print(res)"
  dependsOn:
  - library/modulo/binomial_class.py
  isVerificationFile: true
  path: verify/yosupo_modulo/modulo_binomial_class.test.codon
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/yosupo_modulo/modulo_binomial_class.test.codon
layout: document
redirect_from:
- /verify/verify/yosupo_modulo/modulo_binomial_class.test.codon
- /verify/verify/yosupo_modulo/modulo_binomial_class.test.codon.html
title: verify/yosupo_modulo/modulo_binomial_class.test.codon
---
