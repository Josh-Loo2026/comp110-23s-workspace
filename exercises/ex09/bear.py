"""File to define Bear class."""


class Bear:
    """Creates a bear object and some of its functions."""
    bear_age: int
    hunger_score: int

    def __init__(self):
        """Initializes the object."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Updates the variables to what happens within 1 day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates the hunger score based on how many fish are eaten."""
        self.hunger_score += num_fish
        return None