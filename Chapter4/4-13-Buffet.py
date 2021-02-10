#Define tuple and print
foods = ('pizza', 'squid', 'tribbles', 'algae', '2D Doritos')
print("Original list:")
for food in foods:
    print(food.title())

#Try (unsuccessfully) to modify items in tuple
#foods[0] = 'Tea, Earl Grey, hot'

#Rewrite tuple and print
foods = (
    'hot Earl Grey tea', 'prune juice', 'something green',
    'feline supplement #9', 'chocolate sundae')
print("\nRevised list:")
for food in foods:
    print(food.title())    