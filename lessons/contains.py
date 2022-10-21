"""Example implementing a list utility function"""

# Function name: contains
# We will never have 2 parameters: needle (str), haystack (list[str])
# Return type bool
import turtle


def contains(needle: str, haystack: list[str]) -> bool:
    # Gameplan: 
    # 1. Start with the first index
    i: int = 0
    # 2. Loop through every index
    while i < len(haystack):
        #   2. A test if item at index equal to needle
        if haystack[i] == needle:
            return True
        i += 1
        #       2.A. True return True! We found it!
    return False