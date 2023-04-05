from python_rpg_framework import choice
from pytest import MonkeyPatch as monkeypatch
from io import StringIO

def test_get_choices_for_legitimate_output():
    menu = "options: 1, 2, or 3"
    legal_choices = ("1","2","3")
    result = choice.get_choice(menu, legal_choices)
    assert result in legal_choices

def test_get_choices_for_3():
    menu = "options: 1, 2, or 3"
    legal_choices = ("3")
    result = choice.get_choice(menu, legal_choices)
    assert result in legal_choices
    user_choice = ""
    return user_choice

def test_get_menu_choice_for_legitimate_output(monkeypatch):
    menu = "Options: 1, 2, or 3,"
    legal_choices = ("1","2","3")
    number_input = StringIO('2\n')
    monkeypatch.setattr('sys.stdin', number_input)
    result = choice.get_choice(menu, legal_choices)
    assert result in legal_choices
"""
if __name__ == "__main__":
    print(choice.get_choices("Would you like to A: eat an egg. B: explode an egg.\
                       C: hatch the egg", ("A","B","C")))"""