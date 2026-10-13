"""Three small functions. You write the tests for these in question 4."""


def to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def is_freezing(celsius):
    return celsius <= 0


def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
