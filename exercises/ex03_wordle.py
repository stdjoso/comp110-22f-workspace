"""EX03 - Wordle - The real thing!"""

__author__: str = "730390832"


def contains_char(word: str, letter: str) -> bool:
    """Given a guess, a single character/letter will be searched for at each of index of the guess."""
    assert len(letter) == 1
    char_exists: bool = False 
    i: int = 0
    while not char_exists and i < len(word):   # each index of the first parameter is checked to see if it is equal for the second parameter.
        if word[i] == letter:
            char_exists = True     # true means that the second parameter was found at an index in the guess.
        else:
            i += 1
    return char_exists     # returns bool statement.


def emojified(guess: str, secret: str) -> str:
    """Given a guess and secret of equal length, letters in the guess will be codified with colored emoji boxes."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_result: str = ""
    i: int = 0
    assert len(guess) == len(secret)
    while i < len(guess):   
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:    # secret is the word in the first parameter of contains_char(); guess is searched at each index for equal character/letter in secret/word.
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        i += 1    # ensures while loop is not infinite; reasoning: len-1 = final character index.
    return emoji_result


def input_guess(ex_len: int) -> str:
    """Given an integer that corresponds to a specific length of a word, prompt the user to enter a guess that is the expected length."""
    guess: str = input(f"Enter a {ex_len} character word: ")    # variable is initialized with imput from user.
    while len(guess) != ex_len:
        guess = input(f"That wasn't {ex_len} chars! Try again: ")   
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 1
    user_won: bool = False
    while turns <= 6 and user_won is False:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(SECRET))     # expected len is unbound by a specific number; it is directly related to whatever the length of the "secret" is.
        print(emojified(guess, SECRET))    # printing worldle prior to winning/losing statements.
        if guess == SECRET:  
            user_won = True 
        else:
            turns += 1
    if user_won is True:     # True means that the user's guess equals the secret.
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":     # function can be run as a module and other modules can import functions and reuse them.
    main()