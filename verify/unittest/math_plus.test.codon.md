---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: library/math/plus.py
    title: library/math/plus.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: codon
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/aplusb
  bundledCode: "def plus(a:int,b:int) -> int:\n    \"\"\"oj-verify-helper\u306E\u7DF4\
    \u7FD2\u306E\u305F\u3081\u306B\u4F5C\u3089\u308C\u305F\u7C21\u6613\u306A\u3082\
    \u306E\n    \"\"\"\n    return a+b\n# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb\n\
    \n\nA,B = list(map(int,input().split()))\nprint(plus(A,B))\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/aplusb


    from ...library.math.plus import plus


    A,B = list(map(int,input().split()))

    print(plus(A,B))'
  dependsOn:
  - library/math/plus.py
  isVerificationFile: true
  path: verify/unittest/math_plus.test.codon
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: verify/unittest/math_plus.test.codon
layout: document
redirect_from:
- /verify/verify/unittest/math_plus.test.codon
- /verify/verify/unittest/math_plus.test.codon.html
title: verify/unittest/math_plus.test.codon
---
