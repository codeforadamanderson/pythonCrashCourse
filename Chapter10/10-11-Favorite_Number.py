# Read in a user's favorite number and write it to a json file.
import json

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    favorite_number = input("What is your favorite number? ")
    json.dump(favorite_number, f)