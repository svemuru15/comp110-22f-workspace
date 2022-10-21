"""EX02 - One Shot Wordle An example of wordle software with one try."""

__author__ = "730579372"

# initialization of all important variables
secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
emoji: str = ""
# this is the check for the number of letters in the word
while len(user_guess) != len(secret_word):
    user_guess = input("That was not 6 letters! Try again: ")

# this is for telling you whether your guessed word has the right letters in the right sport
# right letters in the wrong spot
# wrong letters that aren't in the secret word
while index < len(secret_word):
    if user_guess[index] == secret_word[index]:
        emoji += GREEN_BOX
    else:
        diff_loc: bool = False
        alt_index: int = 0
        while not diff_loc and alt_index < len(secret_word):
            if user_guess[index] == secret_word[alt_index]:
                diff_loc = True
            else:
                alt_index += 1
        if diff_loc:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    index += 1

print(emoji)

# final result fo whether guess was correct or not
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")