# TODO: import the madlib function from madlib.py

# TODO: move the madlib function into its own file, madlib.py
def madlib(profession, name, verb, pet, story_continues):
    print(f"There once was a {profession} named {name}.")
    print(f"Every day, {name} would practice {verb} with their pet {pet} by their side.")

    if story_continues:
        print(f"Suddenly, {name} discovered a hidden talent that no one knew about, and everything changed!")
    else:
        print(f"{name} continued their days peacefully, always practicing {verb} with their pet {pet}.")

    print("The end.")


# TODO: replace the hard-coded values with input() calls
def main():
    profession = "Wizard"
    name = "Harry"
    verb = "magic spells"
    pet = "owl"
    story_continues = True

    madlib(profession, name, verb, pet, story_continues)


# TODO: guard this so the story only runs when you run the file directly
main()
