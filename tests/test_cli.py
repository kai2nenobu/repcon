from pathlib import Path

import pytest

from repcon import cli
from tests.helper import read_fixture


@pytest.mark.parametrize("opt", ["--help", "-h"])
def test_help(capsys, opt):
    ret = cli._main([opt])
    out, err = capsys.readouterr()
    assert ret == 0
    assert out.split("\n")[0].startswith("usage: repcon")
    assert err == ""


@pytest.mark.parametrize("opt", ["--version", "-V"])
def test_version(capsys, opt):
    ret = cli._main([opt])
    out, err = capsys.readouterr()
    assert ret == 0
    assert out == "0.0.5\n"
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
    cli._main([str(infile), "--out", str(outfile)])
    out, err = capsys.readouterr()
    assert outfile.read_text() == read_fixture("sonar_generic2.xml")
    assert out == ""
    assert err == ""


def test_success_with_indent_0(capsys):
    infile = Path("tests/fixtures/junit_report2.xml")
    ret = cli._main(["--indent", "0", str(infile)])
    out, err = capsys.readouterr()
    assert ret == 0
    assert out != ""
    assert err == ""


def test_error_when_indent_option_is_negative(capsys):
    ret = cli._main(["--indent", "-1"])
    out, err = capsys.readouterr()
    assert ret == 2
    assert out == "argument -i/--indent: Indentation level must not be negative integer.\n"
    assert err == ""


def test_unknown_arguments(capsys):
    ret = cli._main(["--foo", "--bar"])
    out, err = capsys.readouterr()
    assert ret == 2
    assert out == "unrecognized arguments: --foo --bar\n"
    assert err == ""
