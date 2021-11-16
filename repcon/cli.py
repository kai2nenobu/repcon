from repcon import convert


def main():
    import sys

    if len(sys.argv) < 3:
        print(f"$ {sys.argv[0]} <infile> <outfile>")
        sys.exit(1)
    junit_report = sys.argv[1]
    sonar_report = sys.argv[2]
    with open(junit_report, mode="rt", encoding="utf-8") as infile, open(
        sonar_report, mode="wt", encoding="utf-8"
    ) as outfile:
        input = infile.read()
        outfile.write(convert(input))
    sys.exit(0)


if __name__ == "__main__":
    main()
