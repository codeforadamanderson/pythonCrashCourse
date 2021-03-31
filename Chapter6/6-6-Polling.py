favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

users_to_poll = ('jen', 'sarah', 'joe', 'edward', 'bob', 'phil')

for user in users_to_poll:
    if user in favorite_languages.keys():
        print(f"\nThank you, {user.title()} for taking our poll.")
    elif user not in favorite_languages.keys():
        print(f"\n{user.title()}, please take our poll.")