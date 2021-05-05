filename = 'guest_book.txt'

while True:
    with open(filename, 'a') as file_object:
        name = input("Enter Name (enter 'q' to quit): ")
        if name == 'q':
            break
        else:
            file_object.write(f"{name}\n")