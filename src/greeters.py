from helpers import *
from formal import *


def greet_everyone(names):
    greetings = []
    for name in names:
        greetings.append(greet(name))
    return greetings
