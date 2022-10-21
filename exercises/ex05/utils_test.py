"""EX05 - Unit tests for functions in utils.py."""

__author__ = "730579372"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """This is the test case for an empty string."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_odd() -> None:
    """This tests if the string has only odd numbers."""
    xs: list[int] = [1, 3, 5, 7, 9]
    assert only_evens(xs) == []


def test_only_evens_mixed() -> None:
    """This tests a mix of even and odd numbers."""
    xs: list[int] = [2, 3, 7, 4, 3]
    assert only_evens(xs) == [2, 4]


def test_sub_empty() -> None:
    """This tests an empty string."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_sub_outside_len() -> None:
    """This tests an end value greater the length of the list."""
    xs: list[int] = [4]
    assert sub(xs, 0, 5) == [4]


def test_sub_negative_start() -> None:
    """This tests a negative start value."""
    xs: list[int] = [4, 5, 1, 2, 4]
    assert sub(xs, -1, 3) == [4, 5, 1]


def test_concat_empty() -> None:
    """This tests concatenating two empty strings."""
    xs: list[int] = []
    xr: list[int] = []
    assert concat(xs, xr) == []


def test_concat_one_empty() -> None:
    """This tests concatenation where one string is empty."""
    xs: list[int] = []
    xr: list[int] = [2, 4, 5]
    assert concat(xs, xr) == [2, 4, 5]


def test_concat_both_full() -> None:
    """This tests concatenation of two full strings."""
    xs: list[int] = [2, 4, 1]
    xr: list[int] = [8, 5, 3]
    assert concat(xs, xr) == [2, 4, 1, 8, 5, 3]