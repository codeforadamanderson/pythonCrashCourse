current_users = ['root', 'herobrine', 'admin', 'flynn', 'quark']
new_users = ['steve', 'Quark', 'villager', 'alex', 'Herobrine']
lower_new_users = []

for new_user in new_users:
    lower_new_users.append(new_user.lower())

if new_users:
    for new_user in lower_new_users:
        if new_user in current_users:
            print(f"Username {new_user} taken.  Please pick another name.")
        else:
            print(f"Username {new_user} available.")
else:
    print("No username entered.")