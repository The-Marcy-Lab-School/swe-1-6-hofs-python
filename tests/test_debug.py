from debug import log_each_name, tallest_user

TEST_SUITE_NAME = "Debug Tests"


def printed(capsys):
    lines = []
    for line in capsys.readouterr().out.splitlines():
        if line.strip():
            lines.append(line)
    return lines


def test_log_each_name(capsys):
    """log_each_name - prints each name"""
    log_each_name(["Ada", "Zo", "Bob"])
    assert printed(capsys) == ["Ada", "Zo", "Bob"]


def test_tallest_user():
    """tallest_user - returns the user with the greatest height"""
    users = [
        {"name": "Ada", "height": 22},
        {"name": "Zo", "height": 40},
        {"name": "Bob", "height": 28},
    ]
    assert tallest_user(users) == {"name": "Zo", "height": 40}
