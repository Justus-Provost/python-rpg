

import choice, character, utilities



character_name = ""
character_class = ""
player_dict = {}

def create_character():
    character_name = input("A wise old voice asks: What is your name traveler? You reply: ")
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

def meal_with_old_man():
    print("Come join me for a meal.")
    eat = choice.get_choice("""Do you eat?:
    Here is your list of options:
    1 - Eat
    2 - Don't eat""", ("1", "2"))
    print("""He places a bowl of soup on the table.""")
    if eat == "1":
        print("""After eating the delicious meal you feel refreshed.""")
        player.increase_stat("con", 1)
    else:
        print("You haven't eaten in a ")



def introduction():
    create_character()
    meal_with_old_man()


if __name__ == "__main__":
    player = utilities.get_file_contents("data/", "player.json")
    print(player)
    introduction()
    