usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello, {user}.  Nothing shady going on here at all.")
        else:
            print(f"Hello, {user}.  Days since last de-resolution: 3.")
else:
        print("We need to find some users!")