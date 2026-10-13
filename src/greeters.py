from helpers import *
from formal import *


def greet_everyone(names):
    return [greet(name) for name in names]
