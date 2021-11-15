from repcon import __version__, convert


def test_version():
    assert __version__ == "0.0.1"


def test_conversion():
    input_junit = """\
<?xml version="1.0" encoding="utf-8"?>
<testsuites>
  <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="1" time="0.193">
    <testcase classname="tests.test_repcon" name="test_example" time="0.005" />
  </testsuite>
</testsuites>
"""
    actual = convert(input_junit)
    assert (
        actual
        == """\
<testExecutions version="1">
  <file path="tests/test_repcon.py">
    <testCase name="test_example" duration="5" />
  </file>
</testExecutions>
"""
    )
