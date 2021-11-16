from pathlib import Path


def read_fixture(name: str, encoding="utf-8") -> str:
    path = Path("tests/fixtures", name)
    with open(path, encoding=encoding) as f:
        return f.read()
