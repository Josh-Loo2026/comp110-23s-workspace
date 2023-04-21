"""EX06 - Choose Your Own Adventure."""

__author__ = "730571899"

import random

points: int = 0
player: str = ""
heart: str = " \u2764\uFE0F "
black_heart: str = " \U0001F5A4 "


def main() -> None:
    """This controls all of the other functions and allows the game to run."""
    global points
    global player 
    greet()

    option_prompt: str = input("Please choose a game mode (please note that the options are case sensitive): \n>Survival \n>Wager \n>Exit ")
    while (option_prompt != "Exit"):
        if (option_prompt != "Survival" and option_prompt != "Wager"):
            option_prompt = input("Please enter either Survival, Wager, or Exit. Reminder, these options are case sensitive: ")
        else:
            while (option_prompt == "Survival"):
                coinflip()

                continue_prompt: str = input("Would you like to continue? Please enter Y (representing yes) or N (representing no). ")
                if (continue_prompt != "N" and continue_prompt != "Y"):
                    continue_prompt = input("Please input either Y or N. Reminder, these options are case sensitive: ")
                if (continue_prompt == "N"):
                    option_prompt = input("Would you like to do something else? \n>Survival \n>Wager \n>Exit ")
            
            while (option_prompt == "Wager"):
                if (points > 0):
                    print(f"{player}, your new total points are: {wager(points)}")
                else:
                    print("Sorry! You have no points to wager.")

                continue_prompt: str = input("Would you like to continue? Please enter Y (representing yes) or N (representing no). ")
                if (continue_prompt != "N" and continue_prompt != "Y"):
                    continue_prompt = input("Please input either Y or N. Reminder, these options are case sensitive: ")
                if (continue_prompt == "N"):
                    option_prompt = input("Would you like to do something else? \n>Survival \n>Wager \n>Exit ")
    print(f"Thank you for playing! Your total points were {points}.")


def greet() -> None:
    """This is a function that gives the play a little greeting and explaination on how the games work."""
    global player
    print("Hello! This is a coin flip guessing game.")
    print("There are 2 ways to play: survival or wager")
    print("In survival, you will have 3 lives to guess whether the coin lands on heads or tails.")
    print("If it lands on the correct guess, you will keep your lives and gain a point.")
    print("If it lands on the incorrect guess, you will lose 1 life. You will not gain a point.")
    print("In wager, you will get a certain amount of turns based on the amount of points you currently have.")
    print("If you have no points you will not be able to play.")
    print("After each flip, you will guess whether the coin flipped heads or tails.")
    print("You will gain points for every question you get right. For every question you get wrong, you will lose a point.")
    print("Wager will not affect your over all score. There is no net gain or loss regardless of outcome.")
    player = input("Please input your name: ")


def coinflip() -> None:
    """This is a game in which you have 3 lives and you have to guess the correct outcome each time otherwise you lose a life."""
    global points
    global player
    game_points = 0
    lives: int = 3
    lives_visual: str
    guess: str = input(f"{player} please input H (representing heads) or T (representing tails) for your guess: ")

    while (lives > 1):
        if (guess == "H" or guess == "T" or guess == "h" or guess == "t"):
            rand_num: int = random.randrange(2)
            if (rand_num == 0):
                if (guess == "H" or guess == "h"):
                    print("You guessed correctly! You gain 1 point!")
                    points += 1
                    game_points += 1
                else:
                    print("Sorry, the answer was tails! You guessed incorrectly!")
                    lives -= 1

            if (rand_num == 1):
                if (guess == "T" or guess == "t"):
                    print("You guessed correctly! You gain 1 point!")
                    points += 1
                    game_points += 1
                else:
                    print("Sorry, the answer was heads! You guessed incorrectly!")
                    lives -= 1
            if (lives == 3):
                lives_visual = heart + heart + heart
            if (lives == 2):
                lives_visual = heart + heart + black_heart
            if (lives == 1):
                lives_visual = heart + black_heart + black_heart
            if (lives == 0):
                lives_visual = black_heart + black_heart + black_heart        
        
            print(f"You currently have {points} points and {lives_visual} lives!")
            guess = input("Please input another guess: ")

        else:
            guess = input(f"Your guess {guess} was not H or T! Please input either H or T: ")

    print(f"{player}, you are out of lives! Your point total is {game_points}! Your overall play points are {points}")


def wager(turn_num: int) -> int:
    """You gain or lose points based on if you guess correctly. The amount of turns you get is based on the amount of points you accumulated from Survival."""
    points = turn_num
    game_points: int = 0
    guess: str = input(f"{player} please input H (representing heads) or T (representing tails) for your guess: ")

    while (turn_num > 0):
        if (guess == "H" or guess == "T" or guess == "h" or guess == "t"):
            rand_num: int = random.randrange(2)
            if (rand_num == 0):
                if (guess == "H" or guess == "h"):
                    print("You guessed correctly! You gain 1 point!")
                    game_points += 1
                else:
                    print("Sorry! You guessed incorrectly! You lose 1 point.")
                    game_points -= 1

            if (rand_num == 1):
                if (guess == "T" or guess == "t"):
                    print("You guessed correctly! You gain 1 point!")
                    game_points += 1
                else:
                    print("Sorry! You guessed incorrectly! You lose 1 point.")
                    game_points -= 1
        guess = input("Please input another guess: ")
        turn_num -= 1
    points += game_points

    return points


if __name__ == "__main__":
    main()