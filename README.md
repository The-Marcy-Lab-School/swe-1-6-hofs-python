# Higher-Order Functions

Practice passing functions around.

**Practicing:** callbacks, higher-order functions, `key=`, functions as values

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `my_for_each`](#question-1-my_for_each)
  - [Question 2: `my_map`](#question-2-my_map)
  - [Question 3: `my_filter`](#question-3-my_filter)
  - [Question 4: `my_find`](#question-4-my_find)
  - [Question 5: `describe_longest`](#question-5-describe_longest)
  - [Question 6: `make_announcer`](#question-6-make_announcer)
- [Modify](#modify)
  - [Question 7: `run_menu_choice`](#question-7-run_menu_choice)
  - [Question 8: `safe_int`](#question-8-safe_int)
  - [Question 9: `set_age`](#question-9-set_age)
  - [Question 10: `ask_for_number`](#question-10-ask_for_number)
- [Debug](#debug)
  - [Question 11: `log_each_name`](#question-11-log_each_name)
  - [Question 12: `tallest_user`](#question-12-tallest_user)
  - [Question 13: `load_setting`](#question-13-load_setting)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what the
difference is between `print` and `print()`, or having it quiz you on when to
pass a function and when to call it. Ask it a hundred
questions — that is the whole point. What you do not do is ask it for the
function. Paste this at the start of a chat and it will hold for the rest of
the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
has to say which arguments are functions and what each callback returns. If what
comes back does more than you asked for, reject it — over-delivery is a
defect, and catching it is part of the job.

You own every line either way, and you will be asked to explain it.

## Setup

Clone your repository in `development/mod-1` and then `cd` into it. Set up
your virtual environment and make a draft branch before you start.

```sh
git clone [your_repo]
cd [your_repo]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` to test the entire assignment, or `pytest -k my_map` for one
question. Every push runs the tests on GitHub and reports your score in the
**Actions** tab.

75% of tests passing counts as complete. Submit at that point even if it is
not perfect. Treat submitting as a checkpoint rather than a finish line, and
come back to improve it.

When you are done working on this assignment, turn off your virtual
environment by running:

```sh
deactivate
```

## Before You Start

This assignment has three sections:

1. From Scratch
2. Modify
3. Debug

The single most important thing in the whole assignment:

```python
print       # the function itself
print()     # CALLS it right now, and evaluates to None
```

**Passing `print` hands over the function. Passing `print()` runs it
immediately and hands over `None`, which is not callable.** Two questions here
are a version of that mistake. Watch those parentheses.

## From Scratch

Write your solutions in `src/from_scratch.py`.

### Question 1: `my_for_each`

Write a function `my_for_each` that takes a list `values` and a `callback`. It
should:

- Iterate through the list. On each iteration:
  - Call the `callback` with the value at the current index as its only
    argument
- Not return anything

```python
doubled = []
my_for_each([1, 2, 3], lambda num: doubled.append(num * 2))
# doubled is now [2, 4, 6] — the callback ran once per value
```

This is your own version of a loop somebody else already wrote for you. Four
lines, and then every higher-order function you ever use makes sense.

### Question 2: `my_map`

Write a function `my_map` that takes a list `values` and a `callback`. It
should return a **new** list of what the callback gave back each time.

```python
my_map([1, 2, 3], lambda num: num * 2)
# [2, 4, 6] — each value transformed
my_map(["Alice", "Bob"], len)
# [5, 3] — note that `len` is passed with no parentheses
```

Do not change the original list.

### Question 3: `my_filter`

Write a function `my_filter` that takes a list `values` and a `callback`. It
should return a **new** list of every value the callback said yes to.

```python
my_filter([10, 50, 100], lambda n: n > 50)
# [100] — only 100 passes the test
my_filter([1, 2, 3], lambda n: False)
# [] — nothing passes, so nothing comes back
```

### Question 4: `my_find`

Write a function `my_find` that returns the **first** value the callback says
yes to, or `None` when nothing does.

```python
my_find([1, 2, 3], lambda num: num % 2 == 0)
# 2 — the first even number, and it stops looking there
my_find([1, 3, 5], lambda num: num % 2 == 0)
# None — nothing passed
```

This is important: the **callback** returns `True` or `False`, while the
**higher-order function** returns a value or `None`. Two different jobs, ok?

### Question 5: `describe_longest`

Write a function `describe_longest` that takes a list of words and describes
the longest one.

```python
describe_longest(["hi", "hello", "hey"])
# "hello is 5 letters" — the longest of the three
describe_longest([])
# "no words" — nothing to be longest
```

Hint: `max()` takes a `key=` argument, which is a function it calls on each
value to decide what to compare:

```py
max(users, key=lambda user: user["age"])
```

What function would you hand it to compare words by how long they are?
W3Schools has a [short page on `lambda`](https://www.w3schools.com/python/python_lambda.asp)
if that syntax is new.

### Question 6: `make_announcer`

Write a function `make_announcer` that takes a function and returns a **new**
function. The new one prints `Calling <name>` and then does whatever the
original did.

```python
def add(a, b):
    return a + b

announced = make_announcer(add)
announced(2, 3)
# prints "Calling add", and returns 5
```

Two things make this work. A function knows its own name as `func.__name__`,
and `*args, **kwargs` lets your wrapper accept whatever the wrapped function
accepts and pass it straight along.

The wrapper has to **return** what the wrapped function returned. A wrapper
that forgets is the most common bug in this pattern, because the printing
still looks right.

This is what `@decorator` syntax does underneath. `@make_announcer` above a
definition is another way of writing `add = make_announcer(add)`.

## Modify

Change the function already in `src/modify.py`.

### Question 7: `run_menu_choice`

`run_menu_choice` picks what to do with an `if`/`elif` chain. Replace the
chain with a **dictionary of functions**, keeping the behavior identical.

Do the following:

- Write a small function for each of `add`, `clear` and `count`.
- Put them in a dictionary, with the choice as the key.
- Look the choice up and call what you find.
- Keep returning `"Unknown choice"` for anything not in the dictionary.

The tests check that no `elif` is left.

A function is a value, so it can live in a dictionary exactly like a string
can. Adding a fourth menu option then means adding one entry rather than
editing a chain.

## Debug

### Question 8: `log_each_name`

`log_each_name` should print each name. It prints one blank line and then
raises `TypeError: 'NoneType' object is not callable`.

Look again at the `print` and `print()` box above.

### Question 9: `tallest_user`

`tallest_user` should return the user with the greatest height. It raises a
`TypeError` instead.

```text
TypeError: 'int' object is not callable
```

Read that message literally. Something in the code is trying to call a value
that is a number.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

Once passing functions around feels normal, a huge amount of Python stops
looking like magic. You got this!
