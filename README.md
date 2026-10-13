# Modules, Virtual Environments, and pytest

Practice splitting a program across files, keeping an environment tidy, and
writing the tests instead of only running them.

**Practicing:** modules, imports, `__main__`, JSON, writing tests

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Before You Start](#before-you-start)
- [From Scratch](#from-scratch)
  - [Question 1: `save_scores`](#question-1-save_scores)
  - [Question 2: `load_scores`](#question-2-load_scores)
  - [Question 3: `.gitignore`](#question-3-gitignore)
  - [Question 4: write the tests](#question-4-write-the-tests)
- [Modify](#modify)
  - [Question 5: `modify.py`](#question-5-modifypy)
  - [Question 6: split the madlib](#question-6-split-the-madlib)
- [Debug](#debug)
  - [Question 7: `greeters.py`](#question-7-greeterspy)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what
`__name__` holds when a file is imported, or having it quiz you on what
belongs in `.gitignore` and why. Ask it a hundred questions — that is the
whole point. What you do not do is ask it for the function. Paste this at the
start of a chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
has to say which file each function lives in and what each one imports. If
what comes back does more than you asked for, reject it — over-delivery is a
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

Run `pytest` to test the entire assignment, or `pytest -k madlib` for one
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

You have been running `pytest` since your first assignment. This time you
write some of it. Question 4 asks for three tests of your own, and the grader
runs them.

**Your tests live in `student_tests/`, not in `tests/`.** The grader replaces
`tests/` with its own copy before it runs, so anything you write there is
thrown away. `student_tests/` is yours and is never touched.

If you see `ModuleNotFoundError` at any point, check whether your virtual
environment is on before you check anything else. That error means Python
cannot find a package, and the usual reason is that you are not in the
environment where it was installed.

## From Scratch

### Question 1: `save_scores`

Write a function `save_scores` in `src/scores.py` that takes a file `path` and
a `scores` dictionary, and writes the dictionary to that file as JSON.

```python
save_scores("scores.json", {"Ada": 10, "Zo": 7})
# the file now holds {"Ada": 10, "Zo": 7} as text
```

**JSON** is a text format for data, and almost every program that saves
anything uses it. The `json` module is part of Python's **standard library**,
so it needs importing but not installing. `pytest` is a **third-party
package**, which is why it is in `requirements.txt` and `json` is not.

Hint: `json` has a function that writes straight to an open file, and another
that turns a value into a string. Which one do you want here?

### Question 2: `load_scores`

Write a function `load_scores` in `src/scores.py` that takes a file `path` and
returns the dictionary stored in it.

```python
load_scores("scores.json")
# {"Ada": 10, "Zo": 7} — read back from the file
load_scores("not_there.json")
# {} — no file yet, so no scores yet
```

That second case is the one that matters. A program that saves scores has to
run a first time, when the file does not exist. Crashing is not an answer.

### Question 3: `.gitignore`

Add `.venv/` and `__pycache__/` to `.gitignore` so neither is committed.

`__pycache__` holds the compiled copies Python makes so it can start faster
next time, and `.venv/` holds every installed package. Both are rebuilt from
what you *do* commit: `.venv/` from `requirements.txt`, and `__pycache__`
from your own code.

That is the rule for the whole folder. Commit the recipe, not the meal.

### Question 4: write the tests

Write three tests in `student_tests/test_temperature.py`, one for each
function in `src/temperature.py`. Read that file first.

Do the following:

- Give every test a name starting with `test_` and a **docstring** saying what
  it checks.
- For `is_freezing`, assert the result with `is True` and `is False`.
- For `average`, compare a decimal result with `pytest.approx`.
- Make sure all three pass.

Why those two:

```py
1 == True        # True, because a bool IS an int in Python
1 is True        # False, which is what you wanted to know
0.1 + 0.2 == 0.3 # False, and nothing is wrong with your code
```

`== True` passes for any value equal to 1, so it does not prove you got a
boolean back. And a decimal comparison with `==` fails on arithmetic that is
perfectly correct, which is why `pytest.approx` exists.

Run yours with:

```sh
python3 -m pytest student_tests
```

Hint: `python3 -m pytest` and plain `pytest` are not always the same command.
The first guarantees you are running the pytest inside *this* environment.

## Modify

### Question 5: `modify.py`

`src/modify.py` prints its result at the top level, so that print fires the
moment anybody imports the file. Move it inside an
`if __name__ == "__main__":` guard.

```sh
python3 src/modify.py
# I stand alone. — running it directly still prints
```

Importing it should print nothing at all. Do not delete the print.

`__name__` is a variable Python sets for you. It holds `"__main__"` when you
run the file yourself, and the module's name when somebody imports it. So
that `if` is asking: *am I the file being run, or am I being imported?*

### Question 6: split the madlib

`src/madlib_challenge/main.py` holds two functions. `madlib()` tells a story
and `main()` collects the input.

Do the following:

- Create `src/madlib_challenge/madlib.py`.
- Move the whole `madlib` function into it.
- Import it in `main.py` with `from madlib import madlib`.

One file tells the story, the other talks to the person. That is one concern
each, which is the whole reason to split a file.

Import it **by name**. You may have seen `from madlib import *`, which pulls
in everything a module defines. Question 7 is what happens when you do.

## Debug

### Question 7: `greeters.py`

`greet_everyone` should return the casual greeting from `helpers.py`.

```python
greet_everyone(["Ada"])
# want ["Hey Ada!"], gets ["Good evening, Ada."]
```

Both `helpers.py` and `formal.py` define a function called `greet`, and
`greeters.py` star-imports both. Work out which one wins, and why reading the
file does not tell you without opening the other two.

Fix it so the casual greeting is the one that runs.

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

Every program past a few hundred lines lives in more than one file, and every
one of them has a `.gitignore`. This is the assignment where your projects
start looking like real ones. You got this!
