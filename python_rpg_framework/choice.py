""" choices.py
a set of functions to be used tto make the program more useful and be used 
in other similar projects."""

# import statements
from pathlib import Path

def get_file_contents(path: str, filename: str) -> str:
    """Returns the contents of the file in the path.
    
    Args:
        path: the relative folder path with file name and extentions.(should end with forward slash)
        filename: the name of the file with extention
        
    Returns:
        contents: a string of the file contents."""
    
    folder = Path(path)
    file_to_open = folder / filename
    f = open(file_to_open)
    return f.read()


def get_choice(menu: str, legal_choices: tuple) -> str:
    """displays a menu of options, and asks the user to make a choice.
    
    Args:
        menu: a formatted string of choices for the user
        legal_choices: a tuple of only choices that the user is allowed to make

    Returns:
        user_choice: a single character that must be one of the legal choices

    """

    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_choice = input("Your Choice: ")
        # give feedback if not in legal choices
        if user_choice not in legal_choices:
            print("Sorry that is not an option please choose one of the following:")
            print(legal_choices)
    return user_choice

if __name__ == "__main__":
    contents = get_file_contents("data/", "player.json")
    print(contents)
    menu = "Here is your list of options:\n\t1 - Option #1\n"
    menu+= "\t2 - Option #2\n\t3 - Option #3\n\n"
    selection = get_choice(menu,("1","2","3"))

    print(f"You selected {selection}")

    new_menu = """
    Here is your list of options:
        1 - Option #1: Eat an egg.
        2 - Option #2: Explode an egg.
        3 - Option #3: Hatch an egg.
    """
    options = ("1","2","3")
    new_choice = get_choice(new_menu, options)
    print(f"You selected {selection}")
