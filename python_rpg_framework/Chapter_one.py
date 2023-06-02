

import choice, character


character_name = ""
character_class = ""


def create_character():
    character_name = input("A wise old voice asks: What is your name traveler? You reply:")
    print("You can't fully trust the old man to always give you all the possible options")
    character_class = choice.get_choice("""What is your class, traveler? He asks you:
    Here is your list of options:
    1 - Knight
    2 - Magi""", ("Knight", "Magi", "Warlock"))
    player = character.Character(character_name, character_class)
    print(player.get_stats())
    old_mans_comment(player.strength, character_class)


def old_mans_comment(strength, character_class):
    if strength > 12 and character_class == "Knight":
        print("You look like a strong knight.")
    if strength > 12 and (character_class == "Magi" or character_class == "Warlock"):
        print("You look far too strong to be a Magi.")
    if strength <= 12 and character_class == "Knight":
        print("You don't look like a strong knight.")
    if strength <= 12 and (character_class == "Magi" or character_class == "Warlock"):
        print("You look like proper Magi.")


def introduction():
    create_character()

if __name__ == "__main__":
    introduction()
    