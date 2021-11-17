from pathlib import Path

from repcon import cli
from tests.helper import read_fixture


def test_no_arguments(capsys):
    cli._main([])
    out, err = capsys.readouterr()
    assert out == "$ repcon <infile>\n"
    assert err == ""


def test_only_infile_outputs_stdout(capsys):
    infile = Path("tests/fixtures/junit_report2.xml")
    cli._main([str(infile)])
    out, err = capsys.readouterr()
    assert out == read_fixture("sonar_generic2.xml")
    assert err == ""


def test_both_infile_and_outfile(tmp_path: Path, capsys):
    infile = Path("tests/fixtures/junit_report2.xml")
    outfile = tmp_path / "sonar_report2.xml"
    cli._main([str(infile), str(outfile)])
    out, err = capsys.readouterr()
    assert outfile.read_text() == read_fixture("sonar_generic2.xml")
    assert out == ""
    assert err == ""
