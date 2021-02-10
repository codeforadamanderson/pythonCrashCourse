pizzas = ['cheese', 'pepperoni', 'mushroom', 'pineapple']
for pizza in pizzas:
    print(f"{pizza.capitalize()} is good times.")

print("\nLine one that says something about pizza.")
print("Line two that says something about pizza.")
print("Pizza is good times and stuff.\n")

friend_pizzas = pizzas[:]

pizzas.append('tribble')
friend_pizzas.append('peanut butter')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)