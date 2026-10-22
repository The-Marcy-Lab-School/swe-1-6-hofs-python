from from_scratch import (
    describe_longest,
    make_announcer,
    my_filter,
    my_find,
    my_for_each,
    my_map,
)

TEST_SUITE_NAME = "From Scratch Tests"


def printed(capsys):
    lines = []
    for line in capsys.readouterr().out.splitlines():
        if line.strip():
            lines.append(line)
    return lines


def test_my_for_each():
    """my_for_each - calls the callback on every value and returns nothing"""
    doubled = []
    assert my_for_each([1, 2, 3], lambda n: doubled.append(n * 2)) is None
    assert doubled == [2, 4, 6]

    seen = []
    my_for_each(["a", "b"], seen.append)
    assert seen == ["a", "b"]


def test_my_for_each_does_not_mutate():
    """my_for_each - leaves the original list alone"""
    nums = [1, 2, 3]
    my_for_each(nums, lambda n: n / 2)
    assert nums == [1, 2, 3]

    # repeated so a do-nothing implementation cannot pass this test
    doubled = []
    my_for_each(nums, lambda n: doubled.append(n * 2))
    assert doubled == [2, 4, 6]


def test_my_map():
    """my_map - returns a new list of what the callback returned"""
    assert my_map([1, 2, 3], lambda n: n * 2) == [2, 4, 6]
    assert my_map(["Alice", "Bob"], len) == [5, 3]

    nums = [1, 2, 3]
    my_map(nums, lambda n: n * 2)
    assert nums == [1, 2, 3], "my_map must not change the list it was given."


def test_my_filter():
    """my_filter - returns a new list of the values that pass"""
    assert my_filter([10, 50, 100], lambda n: n > 50) == [100]
    assert my_filter(["ada", "zo", "bob"], lambda w: len(w) == 3) == ["ada", "bob"]
    assert my_filter([1, 2, 3], lambda n: False) == []


def test_my_find():
    """my_find - returns the first value that passes, or None"""
    assert my_find([1, 2, 3], lambda n: n % 2 == 0) == 2
    assert my_find(["ada", "zo", "bobby"], lambda w: len(w) > 3) == "bobby"
    assert my_find([1, 3, 5], lambda n: n % 2 == 0) is None

    # repeated so always returning None cannot pass this test
    assert my_find([1, 3, 5], lambda n: n % 2) == 1


def test_describe_longest():
    """describe_longest - finds the longest word using key="""
    assert describe_longest(["hi", "hello", "hey"]) == "hello is 5 letters"
    assert describe_longest(["a"]) == "a is 1 letters"
    assert describe_longest([]) == "no words"


def test_make_announcer_wraps():
    """make_announcer - returns a function that announces, then calls"""
    def add(a, b):
        return a + b

    announced = make_announcer(add)
    assert callable(announced), "make_announcer should return a function."


def test_make_announcer_returns_the_value(capsys):
    """make_announcer - the wrapper hands back what the wrapped function returned"""
    def add(a, b):
        return a + b

    announced = make_announcer(add)
    result = announced(2, 3)
    assert result == 5, "The wrapper must return the wrapped function's value."
    assert printed(capsys) == ["Calling add"]
