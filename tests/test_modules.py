import importlib.util
import re
import subprocess
import sys
from pathlib import Path

TEST_SUITE_NAME = "Modules Tests"

SRC = Path(__file__).resolve().parent.parent / "src"
CHALLENGE = SRC / "madlib_challenge"


def source(name):
    return (SRC / name).read_text(encoding="utf-8")


def test_modify_is_quiet_on_import():
    """modify.py - prints nothing when another file imports it"""
    result = subprocess.run([sys.executable, "-c", "import modify"],
                            cwd=SRC, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "", (
        "Importing modify.py printed something. Top-level code runs on import."
    )


def test_modify_still_runs_directly():
    """modify.py - keeps its __main__ guard and still prints when run"""
    text = source("modify.py")
    assert re.search(r"""if\s+__name__\s*==\s*['"]__main__['"]\s*:""", text), \
        'modify.py has no if __name__ == "__main__" guard.'

    result = subprocess.run([sys.executable, str(SRC / "modify.py")],
                            capture_output=True, text=True)
    assert "I stand alone." in result.stdout, (
        "Running modify.py directly should still print. Guard it, do not "
        "delete it."
    )


def test_madlib_module_exists():
    """madlib.py - exists and defines a madlib function that runs"""
    path = CHALLENGE / "madlib.py"
    assert path.is_file(), "src/madlib_challenge/madlib.py does not exist yet."

    spec = importlib.util.spec_from_file_location("madlib", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["madlib"] = module
    spec.loader.exec_module(module)

    assert callable(getattr(module, "madlib", None)), \
        "madlib.py does not define a function named madlib."
    module.madlib("Doctor", "Alice", "dance", "cat", True)


def test_main_imports_madlib_by_name():
    """main.py - imports madlib by name instead of defining it"""
    text = (CHALLENGE / "main.py").read_text(encoding="utf-8")

    assert not re.search(r"^\s*def\s+madlib\s*\(", text, re.M), \
        "main.py still defines madlib. Move it to madlib.py."
    assert not re.search(r"^\s*from\s+madlib\s+import\s+\*", text, re.M), \
        "A star import hides where a name came from. Import madlib by name."
    assert re.search(r"^\s*from\s+madlib\s+import\s+madlib\b", text, re.M), \
        "main.py should import madlib by name."


def test_greeters_imports_explicitly():
    """greeters.py - imports the names it uses instead of star importing"""
    text = source("greeters.py")
    assert "import *" not in text, (
        "Two star imports means the second quietly wins. Import by name."
    )


def test_greet_everyone_uses_the_casual_greeting():
    """greet_everyone - uses the greeting from helpers, not formal"""
    sys.path.insert(0, str(SRC))
    for name in ("greeters", "helpers", "formal"):
        sys.modules.pop(name, None)
    from greeters import greet_everyone

    assert greet_everyone(["Ada"]) == ["Hey Ada!"]
    assert greet_everyone(["Ada", "Zo"]) == ["Hey Ada!", "Hey Zo!"]


def test_gitignore_excludes_the_environment():
    """.gitignore - keeps .venv and __pycache__ out of Git"""
    text = (SRC.parent / ".gitignore").read_text(encoding="utf-8")
    assert re.search(r"^\.venv/?\s*$", text, re.M), ".venv is not ignored."
    assert re.search(r"^__pycache__/?\s*$", text, re.M), \
        "__pycache__ is not ignored."
