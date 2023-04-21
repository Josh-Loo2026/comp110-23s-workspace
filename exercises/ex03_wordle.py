"""EX03 - Structured Wordle!"""

__author__ = "730571899"

def contains_char(word: str, letter: str) -> bool:
    """This function takes two string parameters, a word and a character/letter.
    The function then goes through each index to see if the character is found in the word.
    If the character is found, then the function will return a boolean: True. If it is not found
    the function will return a boolean: False."""
    assert len(letter) == 1

    word_len: int = len(word)
    word_idx: int = 0

    while (word_idx < word_len):
        if(word[word_idx] == letter):
            return True
        else:
            word_idx = word_idx + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """This function goes through each index of both the secret word and the word guess.
    If the letter is in the same in both indexes of the secret word and the guess a green box will be added to the string.
    Otherwise, it uses the function contains_char to see whether or not the letter exists within the word.
    If contains_char returns true, it adds a yellow box to the string box. Else it adds a white box."""
    assert len(secret) == len(guess)

    secret_len: int = len(secret)
    secret_idx: int = 0
    box: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    while (secret_idx < secret_len):
        if (secret[secret_idx] == guess[secret_idx]):
            box = box + green_box
        else:
            if (contains_char(secret, guess[secret_idx])):
                box = box + yellow_box
            else:
                box = box + white_box
        secret_idx = secret_idx + 1
    return box

def input_guess(expected_len: int) -> str:
    """It takes the guess based off of the requested character length."""
    word: str = input(f"Enter a {expected_len} character word: ")
    while (len(word) != expected_len):
        word = input(f"That wasn't {expected_len} chars! Try again: ")
    return word

def main() -> None:
    """The entry point of the program and main game loop."""
    guess_amount: int = 1
    secret_word: str = "codes"
    guess: str = ""
    win: bool = False

    while (guess_amount <= 6 and win == False):
        print(f"=== Turn {guess_amount}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if (guess == secret_word):
            win = True
            print(f"You won in {guess_amount}/6 turns!")
        else:    
            guess_amount = guess_amount + 1
    if (guess_amount > 6):
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()