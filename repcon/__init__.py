__version__ = "0.0.1"


def convert(input: str):
    return """\
<testExecutions version="1">
  <file path="tests/test_repcon.py">
    <testCase name="test_example" duration="5" />
  </file>
</testExecutions>
"""
