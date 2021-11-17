from typing import List

from repcon import convert


def _main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("$ repcon <infile> <outfile>")
        return 1
    junit_report = argv[0]
    sonar_report = argv[1]
    with open(junit_report, mode="rt", encoding="utf-8") as infile, open(
        sonar_report, mode="wt", encoding="utf-8"
    ) as outfile:
        input = infile.read()
        outfile.write(convert(input))
    return 0


def main():
    import sys

    sys.exit(_main(sys.argv[1:]))


if __name__ == "__main__":
    main()
