#Define a list of places in the world I'd like to visit.
places = ['London', 'Dublin', 'Paris', 'Berlin', 'San Fransisco', 'Rome']

#Print the list in it's original order.
print("Places I'd like to visit:")
print(places)

#Print list in alphabetical order without modifying list.
print("\nPlaces I'd like to visit in alphabetical order:")
print(sorted(places))

#Show that list has not be modified.
print("\nPlaces I'd like to visit in orginal order:")
print(places)

#Print list in reverse alphabetical order without modifying list.
print("\nPlaces I'd like to visit in reverse alphabetical order:")
print(sorted(places, reverse=True))

#Show that list has not be modified.
print("\nPlaces I'd like to visit in orginal order:")
print(places)

#Sort the list in reverse order and print it.
places.reverse()
print("\nPlaces I'd like to visit permanently sorted in reverse order:")
print(places)

#Sort the list in reverse order again and print it.
places.reverse()
print("\nPlaces I'd like to visit permanently sorted in reverse order again:")
print(places)

#Sort the list in alphabetical order and print it.
places.sort()
print("\nPlaces I'd like to visit permanently sorted in alphabetical order:")
print(places)

#Sort the list in reverse alphabetical order and print it.
places.sort(reverse=True)
print("\nPlaces I'd like to visit permanently sorted in reverse alphabetical order:")
print(places)
