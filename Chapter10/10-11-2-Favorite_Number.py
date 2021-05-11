# Read a favorite number from a json file and display it.
import json

filename = 'favorite_number.json'

with open(filename) as f:
    print(f"I know your favorite number, it's {json.load(f)}.")