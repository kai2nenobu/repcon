import itertools
from typing import List, Optional, cast
from xml.dom import minidom
from xml.etree import ElementTree as ET

__version__ = "0.0.1"


class GenericTestResult:
    def __init__(
        self,
        file: str,
        name: str,
        duration: int,
        result: str,
        short_message: Optional[str] = None,
        long_message: Optional[str] = None,
    ):
        self._file = file
        self.name = name
        self.duration = duration
        self.result = result
        self.short_message = short_message
        self.long_message = long_message

    @property
    def file(self):
        return "{}.py".format(self._file.replace(".", "/"))

    def to_node(self) -> ET.Element:
        node = ET.Element("testCase", attrib={"duration": str(self.duration), "name": self.name})
        if self.result != "ok":
            subnode = ET.Element(self.result, attrib={"message": cast(str, self.short_message)})
            subnode.text = self.long_message
            node.append(subnode)
        return node


def to_test_result(elm: ET.Element) -> GenericTestResult:
    result = GenericTestResult(
        file=elm.get("classname", ""),
        name=elm.get("name", ""),
        duration=int(float(elm.get("time", 0)) * 1000),
        result="ok",
    )
    if elm.find("skipped") is not None:
        subnode = cast(ET.Element, elm.find("skipped"))
        result.result = "skipped"
        result.short_message = subnode.get("message")
        result.long_message = subnode.text
    elif elm.find("failure") is not None:
        subnode = cast(ET.Element, elm.find("failure"))
        result.result = "failure"
        result.short_message = subnode.get("message")
        result.long_message = subnode.text
    return result


def convert(input: str):
    root = ET.fromstring(input)
    generic_cases: List[GenericTestResult] = []
    for suite in root.findall("testsuite"):
        for testcase in suite.findall("testcase"):
            generic_cases.append(to_test_result(testcase))

    def group_by_file(c: GenericTestResult) -> str:
        return c.file

    generic_root = ET.Element("testExecutions", attrib={"version": "1"})
    for file, cases in itertools.groupby(sorted(generic_cases, key=group_by_file), key=group_by_file):
        file_node = ET.Element("file", attrib={"path": file})
        for case in cases:  # type: ignore
            file_node.append(case.to_node())
        generic_root.append(file_node)
    return minidom.parseString(ET.tostring(generic_root)).toprettyxml(encoding="utf-8", indent="    ").decode("utf-8")
