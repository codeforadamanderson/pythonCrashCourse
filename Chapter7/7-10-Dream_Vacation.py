destinations = {}

active = True

while active:
    name = input("\nEnter your name: ")
    destination = input("Enter your desired vacation destination: ")
    prompt = input("What another user like to take the poll (y/n)? ")
    destinations[name] = destination
    if prompt == 'n':
        active = False

for name, destination in destinations.items():
    print(f"\n{name} would like to visit {destination} someday.")