"""EX07 - Unit tests for functions in dictionary.py."""

__author__ = "730579372"


from dictionary import invert, count, favorite_color


def test_one_key_value() -> None:
    """This is the test case for only one key-value pair in dictionary."""
    xs: dict[str, str] = {"kris": "jordan"}
    assert invert(xs) == {"jordan": "kris"}


def test_multiple_key_value() -> None:
    """This is the test case for multiple key-value pairs in dictionary."""
    xs: dict[str, str] = {"kris": "jordan", "sritan": "vemuru", "varsha": "ravisankar"}
    assert invert(xs) == {"jordan": "kris", "vemuru": "sritan", "ravisankar": "varsha"}


def test_same_key_value() -> None:
    """This is the test case for same key-values in dictionary."""
    xs: dict[str, str] = {"jordan": "jordan", "vemuru": "vemuru"}
    assert invert(xs) == {"jordan": "jordan", "vemuru": "vemuru"}


def test_freq_one_all() -> None:
    """This is the test case for all colors having a fequency of one."""
    xs: list[str] = ["purple", "light blue"]
    assert count(xs) == {"purple": 1, "light blue": 1}


def test_one_color() -> None:
    """This is the test case for everyone picking the same color."""
    xs: list[str] = ["purple", "purple", "purple"]
    assert count(xs) == {"purple": 3}


def test_multiple_colors_multiple_freq() -> None:
    """This is the test case for all colors with various frequencies."""
    xs: list[str] = ["purple", "light blue", "purple", "red", "red"]
    assert count(xs) == {"purple": 2, "light blue": 1, "red": 2}


def test_freq_same_mode() -> None:
    """This is the test case for all colors having a fequency of one."""
    xs: dict[str, str] = {"sritan": "purple", "varsha": "light blue"}
    assert favorite_color(xs) == "purple"


def test_multiple_colors_no_tie() -> None:
    """This is the test case for multiple colors being chosen."""
    xs: dict[str, str] = {"sritan": "purple", "varsha": "blue", "sithu": "blue"}
    assert favorite_color(xs) == "blue"


def test_multiple_colors_tie() -> None:
    """This is the test case for all colors with a tie for most."""
    xs: dict[str, str] = {"sritan": "purple", "varsha": "light blue", "sithu": "purple", "sreekar": "red", "sowmya": "red"}
    assert favorite_color(xs) == "purple"