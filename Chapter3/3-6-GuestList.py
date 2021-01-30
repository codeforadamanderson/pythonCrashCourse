guestList = ['Shauna', 'Alyssa', 'Austin', 'Ross']
print("The following will attend or else:")
print(*guestList)
notAvailable = 'Ross'
guestList.remove(notAvailable)
print(f"Unfortuantely, {notAvailable} cannot attend.")
newGuest = 'Rubble'
guestList.append(newGuest)
print("New guest list:")
print(*guestList)
guestList.insert(0,'Sparky')
guestList.insert(3,'Buddy')
guestList.append('Chase')
print("New guests are able to attend.  New guest list:")
print(*guestList)