import pytest

from repcon import __version__, convert
from tests.helper import read_fixture


def test_version():
    assert __version__ == "0.0.6"


@pytest.mark.parametrize(
    "infile,outfile",
    [
        ("junit_report.xml", "sonar_generic.xml"),
        ("junit_report2.xml", "sonar_generic2.xml")
    ]  # fmt: skip
)
def test_conversion(infile, outfile):
    actual = convert(read_fixture(infile), indent=4)
    assert actual == read_fixture(outfile)


def test_conversion_with_indent2():
    actual = convert(read_fixture("junit_report2.xml"), indent=2)
    assert actual == read_fixture("sonar_generic2_i2.xml")
