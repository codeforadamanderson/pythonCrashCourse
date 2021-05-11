# Read in a user's favorite number, write it to a json file, and display it.
import json

def write_number():
    """Read in a user's favorite number and write it to a file."""
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def read_number():
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def show_number():
    favorite_number = read_number()
    if favorite_number:
        print(f"I know your favorite number, it's {favorite_number}.")
    else:
        favorite_number = write_number()
        print(f"We'll remember your favorite number is {favorite_number}.")

show_number()