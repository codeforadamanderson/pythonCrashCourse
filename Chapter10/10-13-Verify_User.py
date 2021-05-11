import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        test = input(f"Are you {username} (Y/N)? ")
        if test.capitalize() == 'N':
            username = get_new_username()
            print("Sorry about that.  "
            f"We'll remember you next time {username}.")
        elif test.capitalize() == 'Y':
            print(f"Welcome back, {username}.")
        else:
            print("You didn't enter a valid response.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()