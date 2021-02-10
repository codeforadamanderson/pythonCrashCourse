my_foods = ['pizza', 'falafel', 'carrot cake', 'tribbles']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("My first three favorite foods are:")
print(my_foods[:3])

print("My middle three favorite foods are:")
print(my_foods[1:4])

print("My last three favorite foods are:")
print(my_foods[-3:])