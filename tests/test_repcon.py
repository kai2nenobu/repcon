from repcon import __version__, convert
from tests.helper import read_fixture


def test_version():
    assert __version__ == "0.0.3"


def test_conversion():
    actual = convert(read_fixture("junit_report.xml"), indent=4)
    assert actual == read_fixture("sonar_generic.xml")


def test_conversion2():
    actual = convert(read_fixture("junit_report2.xml"), indent=4)
    assert actual == read_fixture("sonar_generic2.xml")


def test_conversion_with_indent2():
    actual = convert(read_fixture("junit_report2.xml"), indent=2)
    assert actual == read_fixture("sonar_generic2_i2.xml")
