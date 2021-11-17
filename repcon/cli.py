import argparse
import sys
from typing import List

from repcon import convert


class NonExitArgumentParser(argparse.ArgumentParser):
    """Argument parser not to exit process when an argument parse fails."""

    def __init__(self, *args, **kwargs):
        super(NonExitArgumentParser, self).__init__(*args, **kwargs)

    def error(self, message):
        """Raise ArgumentError instead of exiting process."""
        raise argparse.ArgumentError(argument=None, message=message)


def _print_version():
    from . import __version__

    print(__version__)


def _main(argv: List[str]) -> int:
    parser = NonExitArgumentParser(prog="repcon", description="Desc", add_help=False)
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit.")
    parser.add_argument("-V", "--version", action="store_true", help="Show the version of %(prog)s.")
    parser.add_argument("infile", nargs="?", type=argparse.FileType("rt", encoding="utf-8"), default=sys.stdin)
    parser.add_argument(
        "-o",
        "--out",
        type=argparse.FileType("wt", encoding="utf-8"),
        default=sys.stdout,
        help="Ouput file path. If not specified, output to stdout.",
    )
    try:
        args = parser.parse_args(argv)
        if args.help:
            parser.print_help()
        elif args.version:
            _print_version()
        else:
            inreport = args.infile.read()
            args.out.write(convert(inreport))
        return 0
    except argparse.ArgumentError as e:
        print(str(e))
        return 2


def main():  # pragma: no cover
    sys.exit(_main(sys.argv[1:]))


if __name__ == "__main__":  # pragma: no cover
    main()
