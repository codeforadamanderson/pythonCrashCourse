filename = 'poll_results.txt'

while True:
    with open(filename, 'a') as file_object:
        response = input("Why do you like programming ('q' to quit)? ")
        if response == 'q':
            break
        else:
            file_object.write(f"{response}\n")