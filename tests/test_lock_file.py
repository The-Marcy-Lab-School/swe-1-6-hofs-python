"""Checks the requirements-lock.txt the student generates with pip freeze."""

import re
from pathlib import Path

TEST_SUITE_NAME = "Lock File"

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "requirements-lock.txt"

LINE = re.compile(r"^[A-Za-z0-9._-]+==[0-9][\w.+!-]*$")


def lines():
    if not LOCK.is_file():
        return []
    written = []
    for ln in LOCK.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            written.append(ln)
    return written


def test_lock_file_exists():
    """requirements-lock.txt - the file is there and is not empty"""
    assert LOCK.is_file(), (
        "No requirements-lock.txt yet. Generate it with: "
        "pip freeze > requirements-lock.txt"
    )
    assert lines(), "requirements-lock.txt is empty."


def test_every_line_pins_a_version():
    """requirements-lock.txt - every line pins an exact version with =="""
    written = lines()
    assert written, (
        "No requirements-lock.txt yet. Generate it with: "
        "pip freeze > requirements-lock.txt"
    )
    loose = []
    for ln in written:
        if not LINE.match(ln):
            loose.append(ln)
    assert not loose, (
        "These lines do not pin an exact version: " + ", ".join(loose) +
        ". pip freeze writes name==version for every package."
    )


def test_lists_pytest_and_its_dependencies():
    """requirements-lock.txt - pytest and the packages it installed with it"""
    names = set()
    for ln in lines():
        names.add(ln.split("==")[0].lower())
    assert "pytest" in names, (
        "pytest is not in the lock file. Run pip freeze inside the virtual "
        "environment where you installed it."
    )
    assert len(names) >= 3, (
        f"Only {len(names)} package(s) listed. pip freeze in this environment "
        "shows pytest plus the packages pytest requires."
    )


def test_requirements_txt_is_still_loose():
    """requirements.txt - left as it was, asking for pytest without a version"""
    text = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    assert "pytest" in text, "requirements.txt should still ask for pytest."
    assert "==" not in text, (
        "Leave requirements.txt loose. The exact versions belong in "
        "requirements-lock.txt."
    )
