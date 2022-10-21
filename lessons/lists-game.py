"""Examples of using lists in a simple game."""


from random import randint

rolls: list[int] = list() 

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1,6))

print(rolls)

# remove an item using its index("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")

# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# print(rolls)

# # access an individual item

# print(rolls[0])
# print(rolls[1])

# # access length of list
# print(len(rolls))

# # access last item of a list
# last_index: int = len(rolls) - 1
# print(last_index)