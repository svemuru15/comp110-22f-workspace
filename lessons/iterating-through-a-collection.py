"""examples of looping"""

user_string: str = input("Give me a string!: ")

# variable i is a common counter variable name
# i is short for iteration
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

