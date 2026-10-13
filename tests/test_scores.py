import json
from pathlib import Path

from scores import load_scores, save_scores

TEST_SUITE_NAME = "JSON Tests"


def test_save_scores_writes_json(tmp_path):
    """save_scores - writes a file that json can read back"""
    path = tmp_path / "scores.json"
    save_scores(str(path), {"Ada": 10, "Zo": 7})

    assert path.is_file(), "save_scores did not create the file."
    assert json.loads(path.read_text()) == {"Ada": 10, "Zo": 7}


def test_load_scores_reads_it_back(tmp_path):
    """load_scores - reads a file that save_scores wrote"""
    path = tmp_path / "scores.json"
    save_scores(str(path), {"Ada": 10, "Zo": 7})
    assert load_scores(str(path)) == {"Ada": 10, "Zo": 7}


def test_load_scores_handles_a_missing_file(tmp_path):
    """load_scores - returns an empty dictionary when there is no file yet"""
    assert load_scores(str(tmp_path / "nothing.json")) == {}
