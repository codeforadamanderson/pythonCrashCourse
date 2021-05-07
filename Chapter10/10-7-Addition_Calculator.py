while True:
    print("Enter two integers to have the sum calculated.")
    print("Enter 'q' to quit.")
    num_first = input("\tEnter first integer: ")
    if num_first == 'q':
        break
    num_second = input("\tEnter second integer: ")
    if num_second == 'q':
        break

    try:
        result = int(num_first) + int(num_second)
    except ValueError:
        print("\nWhat are you playing at?\n")
    else:
        print(f"\nThe sum of {num_first} and {num_second} is: {result}\n")