""" character.py
The base class for the player and NPCs. Will have attributes and behavior
common to all characters.
"""


import dm


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
        self.strength = dm.roll_stats()
        self.dexterity = dm.roll_stats()
        self.constitution = dm.roll_stats()
        self.intelligence = dm.roll_stats()

        self.attack_modifier = dm.get_modifier(self.strength)
        self.Acrobatics_modifier = dm.get_modifier(self.dexterity)
        self.Resilience_modifier = dm.get_modifier(self.constitution)
        self.Perception_modifier = dm.get_modifier(self.intelligence)

    def get_stats(self) -> str:
        """return a formatted sting of stats"""

        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexterity}\n"
        stats += f"Constitution: {self.constitution}\n"
        stats += f"Intelligence: {self.intelligence}\n"
        stats += f"Attack Modifier: {self.attack_modifier}\n"
        stats += f"Acrobatics Modifier: {self.Acrobatics_modifier}\n"
        stats += f"Resilience Modifier: {self.Resilience_modifier}\n"
        stats += f"Perception Modifier: {self.Perception_modifier}\n"
        return stats

# global scope
if __name__ == "__main__":
    player = Character("Luciano", "Half-Elf")
    print(player.get_stats())
