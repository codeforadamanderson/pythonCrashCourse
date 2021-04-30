from random import randint

class Die:
    """Create a die"""
    def __init__(self, sides=6):
        """Initialize sides"""
        self.sides = sides
    
    def roll_die(self):
        """Rolls the die"""
        print(f"\nRolling a {self.sides}-sided die 10 times.")
        x = 1
        while x < 11:
            print(f"\tDice roll {x}: {randint(1, self.sides)}")
            x += 1

six_sided_die = Die()
ten_sided_die = Die(10)
twenty_sided_die = Die(20)

six_sided_die.roll_die()
ten_sided_die.roll_die()
twenty_sided_die.roll_die()