---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/modulo/binomial.py
    title: "\u7D20\u6570$mod$\u4E8C\u9805\u4FC2\u6570"
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
    \nfact : list[int]\ninv_fact : list[int]\n\ndef init(n:int,mod:int) -> None:\n\
    \    global fact,inv_fact\n    fact,inv_fact = make_factorial_and_invFactorial_table(n,mod)\n\
    \ndef calc_comb(n:int, k:int, mod:int) -> int:\n    \"\"\"\u4E8C\u9805\u4FC2\u6570\
    nCk\u3092\u7D20\u6570mod\u3067O(1)\u3067\u6C42\u3081\u308B\u95A2\u6570\"\"\"\n\
    \    if n < k:\n        return 0\n    return ((fact[n] * inv_fact[k]) % mod *\
    \ inv_fact[n-k]) % mod\n\ndef calc_comb_998244353(n:int,k:int) -> int:\n    \"\
    \"\"\u4E8C\u9805\u4FC2\u6570nCk\u3092998244353\u3067\u5272\u3063\u305F\u3042\u307E\
    \u308A\u3092O(1)\u3067\u6C42\u3081\u308B\u95A2\u6570\"\"\"\n    if n < k:\n  \
    \      return 0\n    MOD : int = 998244353\n    return ((fact[n] * inv_fact[k])\
    \ % MOD * inv_fact[n-k]) % MOD\n# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    \n\n\nT,mod = list(map(int,input().split()))\n\ninit(min(10**7,mod)-1,mod)\n\n\
    for i in range(T):\n    n,k = list(map(int,input().split()))\n    res = calc_comb(n,k,mod)\n\
    \    print(res)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod\n\
    \n\nfrom ...library.modulo.binomial import init,calc_comb\n\nT,mod = list(map(int,input().split()))\n\
    \ninit(min(10**7,mod)-1,mod)\n\nfor i in range(T):\n    n,k = list(map(int,input().split()))\n\
    \    res = calc_comb(n,k,mod)\n    print(res)"
  dependsOn:
  - library/modulo/binomial.py
  isVerificationFile: true
  path: verify/yosupo_modulo/modulo_binomial.test.codon
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/yosupo_modulo/modulo_binomial.test.codon
layout: document
redirect_from:
- /verify/verify/yosupo_modulo/modulo_binomial.test.codon
- /verify/verify/yosupo_modulo/modulo_binomial.test.codon.html
title: verify/yosupo_modulo/modulo_binomial.test.codon
---
