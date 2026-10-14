"""Checks the tests the student writes in student_tests/test_temperature.py.

This folder is restored from the template before grading, so the student's own
tests live in student_tests/ where they survive. These run that file and
inspect it for the three things question 4 asks for.
"""

import re
import subprocess
import sys
from pathlib import Path

TEST_SUITE_NAME = "Your Tests"

STUDENT = Path(__file__).resolve().parent.parent / "student_tests"
FILE = STUDENT / "test_temperature.py"


def written():
    return FILE.read_text(encoding="utf-8") if FILE.is_file() else ""


def functions(text):
    return re.findall(r"^def (test_\w+)\s*\(", text, re.M)


def test_three_tests_with_docstrings():
    """student tests - three test functions, each with a docstring"""
    text = written()
    names = functions(text)
    assert len(names) >= 3, (
        f"Expected three test functions in student_tests/test_temperature.py, "
        f"found {len(names)}."
    )

    bodies = re.split(r"^def test_\w+\s*\([^)]*\):", text, flags=re.M)[1:]
    missing = []
    for i in range(len(names)):
        body = bodies[i] if i < len(bodies) else ""
        if not re.match(r"\s*(\"\"\"|''')", body):
            missing.append(names[i])
    assert not missing, f"These need a docstring: {', '.join(missing)}"


def test_uses_is_true_or_is_false():
    """student tests - asserts a boolean with `is True` or `is False`"""
    assert re.search(r"\bis\s+(True|False)\b", written()), (
        "One test should assert a boolean with `is True` or `is False`, which "
        "`==` would not catch."
    )


def test_uses_pytest_approx():
    """student tests - compares a decimal with pytest.approx"""
    assert "approx" in written(), (
        "One test should compare a decimal result with pytest.approx."
    )


def test_student_tests_pass():
    """student tests - all of them pass against src/temperature.py"""
    if not functions(written()):
        assert False, "No test functions written yet."

    root = STUDENT.parent
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(FILE), "-q", "-p", "no:cacheprovider"],
        cwd=root, capture_output=True, text=True,
        env={"PYTHONPATH": str(root / "src"), "PATH": "/usr/bin:/bin"},
    )
    assert result.returncode == 0, (
        "Your own tests do not pass:\n" + result.stdout[-1500:]
    )
