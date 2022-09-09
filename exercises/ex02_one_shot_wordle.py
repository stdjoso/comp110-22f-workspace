"""EX02 - One-Shot Wordle - A share-sized Snickers bar step towards Wordle."""

__author__: str = "730390832"

# initializing variables and establishing input while-loop 
SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")     # algorithm can generate output that is specific to any SECRET word I chose 
while len(guess)!= len(SECRET):
    guess = input(f"That was not {len(SECRET)} letters! Try again: ")    # algorithm asks for user input until len(guess) matches len(SECRET); exits while loop when boolean expression is false

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
emoji_result: str = ""

while i < len(guess):   # ensures while loop is not infinite; reasoning: len-1 = final character index
    if guess == SECRET:    # boolean expression/if statement for 100% correct guess 
        while i < len(SECRET): 
            if guess[i] == SECRET[i]:
                emoji_result += GREEN_BOX
                i += 1    # ensures while-loop expression becomes false and breaks; reason 17
        print(emoji_result)
        print("Woo! You got it!")    # established output for 100% correct guess of secret word
    else: 
        while i < len(SECRET):
            if guess[i] == SECRET[i]:
                emoji_result += GREEN_BOX
                i += 1
            else:   
                char_exists: bool = False
                alt_i: int = 0 
                while not char_exists and alt_i < len(SECRET):    # established algorithm to check EACH index for a character in guess that is fround anywhere else in the SECRET
                    if guess[i] == SECRET[alt_i]: 
                         char_exists = True 
                    else: 
                        alt_i += 1   # ensures while-loop expression becomes false and breaks
                if char_exists is True:   # If boolean variable is True, this means that a character in guess was found in alternate indecies in SECRET
                    emoji_result += YELLOW_BOX
                else:
                    emoji_result += WHITE_BOX
                i += 1   # ensures while-loop expression becomes false and breaks
        print(emoji_result)
        print("Not quite. Play again soon!")