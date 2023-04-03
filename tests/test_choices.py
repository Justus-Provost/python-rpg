from python_rpg_framework import choice
def test_get_choices_for_legitimate_output():
    menu = "options: 1, 2, or 3"
    legal_choices = ("1","2","3")
    result = choice.get_choices(menu, legal_choices)
    assert result in legal_choices

def test_get_choices_for_3():
    menu = "options: 1, 2, or 3"
    legal_choices = ("3")
    result = choice.get_choices(menu, legal_choices)
    assert result in legal_choices
    user_choice = ""
    return user_choice

"""
if __name__ == "__main__":
    print(choice.get_choices("Would you like to A: eat an egg. B: explode an egg.\
                       C: hatch the egg", ("A","B","C")))"""