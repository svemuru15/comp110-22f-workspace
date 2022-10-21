"""EX04 - Creating different functions using lists as a tool."""

__author__ = "730579372"


def all(int_list: list[int], int_check: int) -> bool:
    """Checks if all the integers in the list are the same as integer given."""
    if len(int_list) == 0:
        return False
    i: int = 0
    while i < len(int_list):
        if int_list[i] != int_check:
            return False
        else:
            i += 1
    return True


def max(input: list[int]) -> int:
    """This finds the larget int in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max: int = input[0]
    i: int = 0
    while i < len(input):
        if max < input[i]:
            max = input[i]
        i += 1
    return max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """This checks if both of the lists are the exact same."""
    if len(list_one) != len(list_two):
        return False
    i: int = 0
    while i < len(list_one):
        if list_one[i] != list_two[i]:
            return False
        i += 1
    return True