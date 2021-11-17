import sys
from typing import List

from repcon import convert


def _main(argv: List[str]) -> int:
    if len(argv) < 1:
        print("$ repcon <infile>")
        return 1
    infile = open(argv[0], mode="rt", encoding="utf-8")
    outfile = open(argv[1], mode="wt", encoding="utf-8") if len(argv) > 1 else sys.stdout
    input = infile.read()
    outfile.write(convert(input))
    return 0


def main():  # pragma: no cover
    sys.exit(_main(sys.argv[1:]))


if __name__ == "__main__":  # pragma: no cover
    main()
