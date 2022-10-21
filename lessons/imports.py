"""Examples of importing in python"""

from lessons import helpers
from lessons import helpers as hp

def main() -> None:
    """Entry point of program"""
    print(hp.powerful(2,4))
    print(f"The answer: {hp.THE_ANSWER}")


if __name__ == "__main__":
    main()