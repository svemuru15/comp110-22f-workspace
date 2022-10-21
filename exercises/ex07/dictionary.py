"""EX07 - Creating functions using dictionaries."""

__author__ = "730579372"


def invert(a: dict[str, str]) -> dict[str, str]:
    """This inverts a dictionary to switch the key and value places."""
    x: dict[str, str] = {}
    for i in a:
        value: str = a[i]
        if value in x:
            raise KeyError("There are two keys with the same value")
        else:
            x[value] = i
    return x


def count(a: list[str]) -> dict[str, int]:
    """This counts the frequencies of strings in the list."""
    times: dict[str, int] = {}
    for i in a:
        if i in times:
            times[i] += 1
        else:
            times[i] = 1
    return times


def favorite_color(a: dict[str, str]) -> str:
    """This will return the most picked color from the dictionary."""
    times: dict[str, int] = {}
    for i in a:
        if a[i] in times:
            times[a[i]] += 1
        else:
            times[a[i]] = 1
    mode: int = 0
    for color in times:
        if times[color] > mode:
            mode = times[color]
    for fav_color in times:
        if times[fav_color] == mode:
            return fav_color
    return fav_color