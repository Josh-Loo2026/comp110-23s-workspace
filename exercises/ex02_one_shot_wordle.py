"""EX02 - One-Shot Wordle - Loop!"""

__author__ = "730571899"

secret_word: str = "python"
secret_len: int = len(secret_word)
guess: str = input(f"What is your {secret_len}-letter guess? ")
idx_num: int = 0
secret_idx: int = 0
exists: bool = False
box: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


while (len(guess) != secret_len):
    guess = input(f"That was not {secret_len}-letters! Try again: ")

while (idx_num < secret_len):
    if (guess[idx_num] == secret_word[idx_num]):
        box = box + green_box
    else:
        while (secret_idx < secret_len):
            if (secret_word[secret_idx] == guess[idx_num]):
                exists = True
                secret_idx = secret_idx + 1
            else:
                secret_idx = secret_idx + 1

        if (exists):
            box = box + yellow_box
        else:
            box = box + white_box
        exists = False
        secret_idx = 0
    idx_num = idx_num + 1

if (guess != secret_word):
    print(box)
    print("Not quite. Play again soon!")
else:
    print(box)
    print("Woo! You got it!")