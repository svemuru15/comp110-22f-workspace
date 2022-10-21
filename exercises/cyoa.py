"""EX06 - Choose your own adventure number guess game."""

__author__ = "730579372"


import random


points: int = 100
player: str = ""
level: int = 0
THUMBS_UP: str = "\U0001F44D"
THUMBS_DOWN: str = "\U0001F44E"


def main() -> None:
    """Main function that runs the game using all the functions created in code."""
    global level
    global points
    greet()
    mode()
    if level == 1:
        points = elementary(points)
    elif level == 2:
        points = middle(points)
    elif level == 3:
        points = high(points)
    play_again: bool = True
    while play_again:
        user_play: str = input("Do you want to play again? Or you can type c for a mystery challenge question! (y/n/c): ")
        if user_play == "y":
            mode()
            if level == 1:
                points = elementary(points)
            elif level == 2:
                points = middle(points)
            elif level == 3:
                points = high(points)
        elif user_play == "c":
            print("This is a challenge question if you get this right you double your points or else you lose all of them!")
            challenge_answer: str = input("What is the integral of 15? ")
            if challenge_answer == "15x + c":
                points *= 2
                print(f"Congratss! You earned {points} iq points!")
                play_again = False
            else:
                print("You got it wrong. You earned 0 iq points.")
                play_again = False
        elif user_play == "n":
            print(f"Thanks for playing! You earned {points} iq points.")
            play_again = False


def greet() -> None:
    """Greet function that gets the players name and gives background of the game."""
    global player
    player = input("What's your name? ")
    print(f"Hello {player} Today you will play a game to test your math skills. As you answer tougher questions you earn more IQ points. Depending on your difficulty choice you will get a math question to do.")


def mode() -> None:
    """Helps the player select the difficulty mode they want to play."""
    global level
    level = int(input(f"Hello {player}, do you want to play at elementary(1), middle(2), or high school and beyond difficulty(3)? "))
    if level == 1:
        print("You will get elementary school difficulty.")
    elif level == 2:
        print("You will get middle school difficulty.")
    elif level == 3: 
        print("You will get high school and beyond difficulty.")


def elementary(iq: int) -> int:
    """Ask the question for elementary difficulty mode."""
    points: int = iq
    turns: int = 0
    right_answer: bool = True
    x: int = random.randint(5, 10)
    y: int = random.randint(1, 5)
    answer: int = x - y
    player_answer: int = int(input(f"What is {x} minus {y}? "))
    while right_answer:
        if player_answer != answer:
            player_answer = int(input(f"That's not right{THUMBS_DOWN}. Try again: "))
            turns += 1
            points -= 10
        else:
            turns += 1
            print(f"That's right{THUMBS_UP}! It took you {turns} attempts(s).")
            points += 20
            right_answer = False
            return points
    return points


def middle(iq: int) -> int:
    """Asks the questions for middle school difficulty mode."""
    points: int = iq
    turns: int = 0
    right_answer: bool = True
    x: int = random.randint(1, 10)
    y: int = random.randint(1, 10)
    answer: int = (x * y) - x
    player_answer: int = int(input(f"What is {x} times {y} minus {x}? "))
    while right_answer:
        if player_answer != answer:
            player_answer = int(input(f"That's not right{THUMBS_DOWN}. Try again: "))
            turns += 1
            points -= 10
        else:
            turns += 1
            print(f"That's right{THUMBS_UP}! It took you {turns} attempts(s).")
            points += 40
            right_answer = False
            return points
    return points


def high(iq: int) -> int:
    """Asks the question for high school difficulty."""
    points: int = iq
    turns: int = 0
    right_answer: bool = True
    x: int = random.randint(1, 10)
    y: int = random.randint(1, 10)
    answer: int = y
    player_answer: int = int(input(f"What is the derivative of {y}x plus {x} with respect to x? "))
    while right_answer:
        if player_answer != answer:
            player_answer = int(input(f"That's not right{THUMBS_DOWN}. Try again: "))
            turns += 1
            points -= 10
        else:
            turns += 1
            print(f"That's right{THUMBS_UP}! It took you {turns} attempt(s).")
            points += 60
            right_answer = False
            return points
    return points


if __name__ == "__main__":
    main()