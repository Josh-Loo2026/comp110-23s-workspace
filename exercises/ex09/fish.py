"""File to define Fish class."""

class Fish:
    """Creates a fish and some of its functions."""
    fish_age: int


    def __init__(self):
        """Initializes the object."""
        self.age = 0
        return None
    

    def one_day(self):
        """Updates the variables to what happens within 1 day."""
        self.age += 1
        return None