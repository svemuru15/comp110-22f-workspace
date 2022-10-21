"""EX05 - Creating different functions to be tested."""

__author__ = "730579372"


def only_evens(xs: list[int]) -> list[int]:
    """Makes a new list with only the even numbers of the inputted list."""
    evens_list: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens_list.append(xs[i])
        i += 1
    return evens_list


def concat(first: list[int], second: list[int]) -> list[int]:
    """Makes a new list that comeines the two input lists."""
    combine_list: list[int] = list()
    i: int = 0
    while i < len(first):
        combine_list.append(first[i])
        i += 1
    i = 0
    while i < len(second):
        combine_list.append(second[i])
        i += 1
    return combine_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Makes a new list that is a subset of the inputted list."""
    subset: list[int] = list()
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)
    if len(xs) == 0:
        return subset
    if start > len(xs):
        return subset
    if end == 0:
        return subset
    while start < end:
        subset.append(xs[start])
        start += 1
    return subset