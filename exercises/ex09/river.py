"""File to define River class."""

__author__ = "730571899"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

class River:
    
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_bear_list: list[Bear] = self.bears
        new_fish_list: list[Fish] = self.fish

        for idx in self.fish:
            if (idx.age > 3):
             new_fish_list.pop()
        for idx in self.bears:
            if (idx.age > 5):
             new_bear_list.pop()
        self.fish = new_fish_list
        self.bears = new_bear_list
        return None

    def bears_eating(self):
        for idx in self.bears:
            if (5 <= len(self.fish)):
                self.remove_fish(3)
                idx.eat(3)
        return None
    
    def check_hunger(self):
        new_bear_list: list[Bear] = self.bears
        for x in new_bear_list:
            if(x.hunger_score < 0):
                new_bear_list.pop()
        self.bears = new_bear_list
        return None
        
    def repopulate_fish(self):
        fish_reproduction: int = (len(self.fish) // 2 * 4)
        for idx in range(0, fish_reproduction):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        bear_reproduction: int = len(self.bears) // 2
        idx: int = 0
        while idx < bear_reproduction:
            self.bears.append(Bear())
            idx += 1
        return None
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~ \nFish population: {len(self.fish)} \nBear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


    def one_river_week(self):
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

    def remove_fish(self, amount: int) -> None:
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1