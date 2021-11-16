from xml.dom import minidom
from xml.etree import ElementTree as ET

__version__ = "0.0.1"


def convert(input: str):
    root = ET.Element("testExecutions", attrib={"version": "1"})
    file = ET.SubElement(root, "file", attrib={"path": "tests/test_repcon.py"})
    ET.SubElement(file, "testCase", attrib={"duration": "5", "name": "test_example"})
    return minidom.parseString(ET.tostring(root)).toprettyxml(encoding="utf-8", indent="  ").decode("utf-8")


# <testExecutions version="1">
#  <file path="tests/test_repcon.py">
#    <testCase name="test_example" duration="5" />
#  </file>
# </testExecutions>
