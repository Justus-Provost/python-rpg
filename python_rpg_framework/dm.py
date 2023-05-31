"""dm.py: The Dungeon Master (DM) for our program"""

import random


def roll_stats() -> int:
    """get stats for a characters attributes
    
    Standard Algorithm in DnD: FTW (For the win)
        Roll a 6-sided die 4 times.
        drop the lowest score.
        Add the remaining numbers.
    
    Simplified algorithm:
    simulate that behavior from above: 
    return a random number between 6 and 18"""
    # My attempt (authentic method)
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    stats = roll1 + roll2 + roll3 + roll4
    
    # Removing the smallest roll
    
    temp = roll1
    if temp <= roll2:
        pass
    else:
        temp = roll2
    if temp <= roll3:
        pass
    else:
        temp = roll3
    if temp <= roll4:
        pass
    else:
        temp = roll4
    ability_score = stats - temp
    return ability_score


def get_modifier(stat: int) -> int:
    """returns a modifier for a stat."""
    modifier = 0
    return modifier


    
