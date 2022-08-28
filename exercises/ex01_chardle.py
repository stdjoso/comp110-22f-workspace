"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730390832"

five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1: 
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_char + " in " + five_char_word)

if single_char == five_char_word[0]:
    print(single_char + " found at index 0")
if single_char == five_char_word[1]:
    print(single_char + " found at index 1")
if single_char == five_char_word[2]:
    print(single_char + " found at index 2")
if single_char == five_char_word[3]:
    print(single_char + " found at index 3")
if single_char == five_char_word[4]:
    print(single_char + " found at index 4")

count: int = 0
if single_char == five_char_word[0]:
    count += 1
if single_char == five_char_word[1]:
    count += 1
if single_char == five_char_word[2]:
    count += 1
if single_char == five_char_word[3]:
    count += 1
if single_char == five_char_word[4]:
    count += 1
if count == 1:
    print(str(count) + " instance of " + single_char + " found in " + five_char_word)
else:
    if count > 1:
        print(str(count) + " instances of " + single_char + " found in " + five_char_word)
    if count == 0:
        print("No instances of " + single_char + " found in " + five_char_word)