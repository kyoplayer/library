---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/math/factorial.py
    title: "\u968E\u4E57, \u9006\u968E\u4E57, \u305D\u306E\u4E21\u65B9(make tables)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: codon
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/challenges/sources/PCK/Prelim/0019
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
    # verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/challenges/sources/PCK/Prelim/0019\n\
    \n\nN : int = int(input())\nfact = make_factorial_table(N,8999999999999999983)\n\
    print(fact[N])\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/challenges/sources/PCK/Prelim/0019


    from ...library.math.factorial import make_factorial_table


    N : int = int(input())

    fact = make_factorial_table(N,8999999999999999983)

    print(fact[N])'
  dependsOn:
  - library/math/factorial.py
  isVerificationFile: true
  path: verify/unittest/math_factorial.test.codon
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/unittest/math_factorial.test.codon
layout: document
redirect_from:
- /verify/verify/unittest/math_factorial.test.codon
- /verify/verify/unittest/math_factorial.test.codon.html
title: verify/unittest/math_factorial.test.codon
---
