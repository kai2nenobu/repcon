import argparse
import sys
from typing import List

from repcon import convert


def _main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(prog="repcon", add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit.")
    parser.add_argument("infile", nargs="?", type=argparse.FileType("rt", encoding="utf-8"), default=sys.stdin)
    parser.add_argument(
        "-o",
        "--out",
        type=argparse.FileType("wt", encoding="utf-8"),
        default=sys.stdout,
        help="Ouput file path. If not specified, output to stdout.",
    )
    args = parser.parse_args(argv)
    if args.help:
        parser.print_help()
        return 0
    input = args.infile.read()
    args.out.write(convert(input))
    return 0


def main():  # pragma: no cover
    sys.exit(_main(sys.argv[1:]))


if __name__ == "__main__":  # pragma: no cover
    main()
