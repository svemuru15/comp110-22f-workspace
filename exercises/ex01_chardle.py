"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730579372"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_char: str = input("Enter a single character: ")
if len(user_char) != 1:
    print("Error: Character must be a single character.")
    exit()
counter: int = 0

print("Searching for " + user_char + " in " + user_word)

if user_word[0] == user_char:
    print(user_char + " found at index 0")
    counter = counter + 1
if user_word[1] == user_char:
    print(user_char + " found at index 1")
    counter = counter + 1
if user_word[2] == user_char:
    print(user_char + " found at index 2")
    counter = counter + 1
if user_word[3] == user_char:
    print(user_char + " found at index 3")
    counter = counter + 1
if user_word[4] == user_char:
    print(user_char + " found at index 4")
    counter = counter + 1
if counter = 0:
    print("No instances of " + user_char + " found in " + user_word)
else:
    if counter = 1:
        print(counter + " instance of " + user_char + " found in " + user_word)
    else:
        print(counter + " instances of " + user_char + " found in " + user_word)