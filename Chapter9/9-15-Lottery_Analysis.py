from random import choice

my_ticket = (1, 3, 5, 7, 9, 'a', 'b', 'c', 'd', 'e')

counter = 1

while choice(my_ticket) != 1:
    counter += 1

print(f"Number of tries to win: {counter}.")