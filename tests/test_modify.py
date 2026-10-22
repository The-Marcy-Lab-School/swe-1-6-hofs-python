from modify import run_menu_choice

TEST_SUITE_NAME = "Modify Tests"


def test_run_menu_choice_uses_a_dictionary():
    """run_menu_choice - behaves the same, without an if/elif chain"""
    import inspect

    source = inspect.getsource(run_menu_choice)
    assert "elif" not in source, (
        "Replace the if/elif chain with a dictionary of functions."
    )

    tasks = []
    assert run_menu_choice("add", tasks) == "1 task(s)"
    assert run_menu_choice("add", tasks) == "2 task(s)"
    assert run_menu_choice("count", tasks) == "2 task(s)"
    assert run_menu_choice("clear", tasks) == "0 task(s)"
    assert run_menu_choice("nonsense", tasks) == "Unknown choice"
