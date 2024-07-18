import random

def roll_dice(number_of_dice):
    # Initialize the total score
    score = 0
    
    # Roll each die and add its value to the score
    for _ in range(number_of_dice):
        score += random.randint(1, 6)
    
    # Return the total score
    return score

# Test cases
assert roll_dice(0) == 0
assert roll_dice(1000) != roll_dice(1000)

# Extensive testing for various numbers of dice
for i in range(1000):
    assert 1 <= roll_dice(1) <= 6
    assert 2 <= roll_dice(2) <= 12
    assert 3 <= roll_dice(3) <= 18
    assert 100 <= roll_dice(100) <= 600