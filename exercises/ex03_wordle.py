"""EX03 - Wordle where the actual wordle software is represented."""

__author__ = "730579372"


def contains_char(searched_str: str, search_char: str) -> bool:
    """Search to see if the character is anywhere in the initial string."""
    index: int = 0
    assert (len(search_char)) == 1
    # runs through the word to check for the character
    while index < len(searched_str):
        if search_char == searched_str[index]:
            return True        
        else:
            index += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Create an emoji string based on if a character is in the right place, wrong place, or wrong character."""
    assert len(secret_word) == len(user_guess)
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    while index < len(secret_word):
        # this is for the right character in the right place to add a green box
        if user_guess[index] == secret_word[index]:
            emoji += GREEN_BOX
        else:
            # this adds yellow for right character wrong place
            if contains_char(secret_word, user_guess[index]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(guess_len: int) -> str:
    """Makes sure that guesses are the right number of characters."""
    guess: str = input(f"Enter a {guess_len} character word: ")
    if len(guess) == guess_len:
        return guess
    else:
        while len(guess) != guess_len:
            guess = input(f"That wasn't {guess_len} chars! Try again: ")
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # initializes variable for number of turns
    turn: int = 1
    # initializes the solution
    secret_word: str = "codes"
    # variable to help stop while loop if the guess is correct
    guess_incorrect: bool = True
    while turn <= 6 and guess_incorrect:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn}/6 turns!")
            guess_incorrect = False
        else:
            turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()