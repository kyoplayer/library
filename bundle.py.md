---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes: {}
  bundledCode: "from __future__ import annotations\n\nimport pathlib\nimport re\n\
    import sys\n\nimport onlinejudge_verify.languages.list # type: ignore\n\nLIBRARY_IMPORT_RE\
    \ = re.compile(\n    r\"^\\s*from\\s+(?:\\.\\.\\.library\\.|library\\.library\\\
    .)\"\n)\n\n\ndef remove_library_imports(data: bytes) -> bytes:\n    result = []\n\
    \n    for line in data.splitlines(keepends=True):\n        text = line.decode()\n\
    \n        if LIBRARY_IMPORT_RE.match(text):\n            continue\n\n        result.append(line)\n\
    \n    return b\"\".join(result)\n\n\ndef bundle_recursive(\n    path: pathlib.Path,\n\
    \    visited: set[pathlib.Path],\n) -> bytes:\n    path = path.resolve()\n\n \
    \   if path in visited:\n        return b\"\"\n\n    visited.add(path)\n\n   \
    \ language = onlinejudge_verify.languages.list.get(path)\n\n    if language is\
    \ None:\n        raise RuntimeError(f\"Unsupported language: {path}\")\n\n   \
    \ result = bytearray()\n\n    # list_dependencies() \u306E\u5148\u982D\u306F\u81EA\
    \u5206\u81EA\u8EAB\n    dependencies = language.list_dependencies(\n        path,\n\
    \        basedir=pathlib.Path(\".\"),\n    )[1:]\n\n    # \u4F9D\u5B58\u5148\u3092\
    \u5148\u306B\u5C55\u958B\n    for dependency in dependencies:\n        result.extend(\n\
    \            bundle_recursive(\n                pathlib.Path(dependency),\n  \
    \              visited,\n            )\n        )\n\n    data = path.read_bytes()\n\
    \n    # \u30E9\u30A4\u30D6\u30E9\u30EA\u306E import \u306F\u5C55\u958B\u6E08\u307F\
    \u306A\u306E\u3067\u524A\u9664\n    if path.suffix in {\".py\", \".codon\"}:\n\
    \        data = remove_library_imports(data)\n\n    result.extend(data)\n\n  \
    \  if data and not data.endswith(b\"\\n\"):\n        result.extend(b\"\\n\")\n\
    \n    return bytes(result)\n\n\ndef main() -> None:\n    if len(sys.argv) != 2:\n\
    \        print(\n            f\"usage: {pathlib.Path(sys.argv[0]).name} <path>\"\
    ,\n            file=sys.stderr,\n        )\n        sys.exit(1)\n\n    path =\
    \ pathlib.Path(sys.argv[1])\n\n    if not path.is_file():\n        print(f\"file\
    \ not found: {path}\", file=sys.stderr)\n        sys.exit(1)\n\n    sys.stdout.buffer.write(\n\
    \        bundle_recursive(\n            path,\n            visited=set(),\n  \
    \      )\n    )\n\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "from __future__ import annotations\n\nimport pathlib\nimport re\nimport sys\n\
    \nimport onlinejudge_verify.languages.list # type: ignore\n\nLIBRARY_IMPORT_RE\
    \ = re.compile(\n    r\"^\\s*from\\s+(?:\\.\\.\\.library\\.|library\\.library\\\
    .)\"\n)\n\n\ndef remove_library_imports(data: bytes) -> bytes:\n    result = []\n\
    \n    for line in data.splitlines(keepends=True):\n        text = line.decode()\n\
    \n        if LIBRARY_IMPORT_RE.match(text):\n            continue\n\n        result.append(line)\n\
    \n    return b\"\".join(result)\n\n\ndef bundle_recursive(\n    path: pathlib.Path,\n\
    \    visited: set[pathlib.Path],\n) -> bytes:\n    path = path.resolve()\n\n \
    \   if path in visited:\n        return b\"\"\n\n    visited.add(path)\n\n   \
    \ language = onlinejudge_verify.languages.list.get(path)\n\n    if language is\
    \ None:\n        raise RuntimeError(f\"Unsupported language: {path}\")\n\n   \
    \ result = bytearray()\n\n    # list_dependencies() \u306E\u5148\u982D\u306F\u81EA\
    \u5206\u81EA\u8EAB\n    dependencies = language.list_dependencies(\n        path,\n\
    \        basedir=pathlib.Path(\".\"),\n    )[1:]\n\n    # \u4F9D\u5B58\u5148\u3092\
    \u5148\u306B\u5C55\u958B\n    for dependency in dependencies:\n        result.extend(\n\
    \            bundle_recursive(\n                pathlib.Path(dependency),\n  \
    \              visited,\n            )\n        )\n\n    data = path.read_bytes()\n\
    \n    # \u30E9\u30A4\u30D6\u30E9\u30EA\u306E import \u306F\u5C55\u958B\u6E08\u307F\
    \u306A\u306E\u3067\u524A\u9664\n    if path.suffix in {\".py\", \".codon\"}:\n\
    \        data = remove_library_imports(data)\n\n    result.extend(data)\n\n  \
    \  if data and not data.endswith(b\"\\n\"):\n        result.extend(b\"\\n\")\n\
    \n    return bytes(result)\n\n\ndef main() -> None:\n    if len(sys.argv) != 2:\n\
    \        print(\n            f\"usage: {pathlib.Path(sys.argv[0]).name} <path>\"\
    ,\n            file=sys.stderr,\n        )\n        sys.exit(1)\n\n    path =\
    \ pathlib.Path(sys.argv[1])\n\n    if not path.is_file():\n        print(f\"file\
    \ not found: {path}\", file=sys.stderr)\n        sys.exit(1)\n\n    sys.stdout.buffer.write(\n\
    \        bundle_recursive(\n            path,\n            visited=set(),\n  \
    \      )\n    )\n\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn: []
  isVerificationFile: false
  path: bundle.py
  requiredBy: []
  timestamp: '2026-10-04 14:09:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: bundle.py
layout: document
redirect_from:
- /library/bundle.py
- /library/bundle.py.html
title: bundle.py
---
