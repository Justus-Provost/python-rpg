""" character.py
The base class for the player and NPCs. Will have attributes and behavior
common to all characters.
"""

class Character:
    """Any playing and non-playing character share these traits
    
    Attributes:
        name: a string
        class_name: string name of character class
        
        max and temporary health: both ints
        speed: an int
        strength: an int physical power and carrying capacity
        dexterity: an int agility, balance, coordination
        constitution: int endurance, stamina, health
        intelligence: int reasoning, knowledge, memory
        armor class/defence: an int
        race: a string
        (maybe)appearance/description: a string/ascii art
        . . . and so on (you choose which of these you want)"""
    

    def __init__(self, name: str, class_name="") -> None:
        self.name = name
        self.class_name = class_name

        # initialize all remaining stats to 0 (we'll create a funtion to set them)
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0

    def get_stats(self) -> str:
        """return a formatted sting of stats"""

        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexterity}\n"
        stats += f"Constitution: {self.constitution}\n"
        stats += f"Intelligence: {self.intelligence}\n"
        return stats

# global scope
if __name__ == "__main__":
    player = Character("Luciano", "Half-Elf")
    print(player.get_stats())
