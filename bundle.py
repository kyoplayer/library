from __future__ import annotations

import pathlib
import re
import sys

import onlinejudge_verify.languages.list # type: ignore

LIBRARY_IMPORT_RE = re.compile(
    r"^\s*from\s+(?:\.\.\.library\.|library\.library\.)"
)


def remove_library_imports(data: bytes) -> bytes:
    result = []

    for line in data.splitlines(keepends=True):
        text = line.decode()

        if LIBRARY_IMPORT_RE.match(text):
            continue

        result.append(line)

    return b"".join(result)


def bundle_recursive(
    path: pathlib.Path,
    visited: set[pathlib.Path],
) -> bytes:
    path = path.resolve()

    if path in visited:
        return b""

    visited.add(path)

    language = onlinejudge_verify.languages.list.get(path)

    if language is None:
        raise RuntimeError(f"Unsupported language: {path}")

    result = bytearray()

    # list_dependencies() の先頭は自分自身
    dependencies = language.list_dependencies(
        path,
        basedir=pathlib.Path("."),
    )[1:]

    # 依存先を先に展開
    for dependency in dependencies:
        result.extend(
            bundle_recursive(
                pathlib.Path(dependency),
                visited,
            )
        )

    data = path.read_bytes()

    # ライブラリの import は展開済みなので削除
    if path.suffix in {".py", ".codon"}:
        data = remove_library_imports(data)

    result.extend(data)

    if data and not data.endswith(b"\n"):
        result.extend(b"\n")

    return bytes(result)


def main() -> None:
    if len(sys.argv) != 2:
        print(
            f"usage: {pathlib.Path(sys.argv[0]).name} <path>",
            file=sys.stderr,
        )
        sys.exit(1)

    path = pathlib.Path(sys.argv[1])

    if not path.is_file():
        print(f"file not found: {path}", file=sys.stderr)
        sys.exit(1)

    sys.stdout.buffer.write(
        bundle_recursive(
            path,
            visited=set(),
        )
    )


if __name__ == "__main__":
    main()