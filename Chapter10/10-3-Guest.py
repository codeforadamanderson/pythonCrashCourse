filename = 'guest.txt'

with open(filename, 'a') as file_object:
    name = input("Enter Name: ")
    file_object.write(f"{name}\n")