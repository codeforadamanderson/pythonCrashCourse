prompt = "Enter your age (enter 0 to quit): "
age = 100
active = True

while active:
    age = input(prompt)
    age = int(age)
    if age == 0:
        active = False
    elif age < 3:
        print("Ticket cost: $0")
    elif age < 13:
        print("Ticket cost: $10")
    else:
        print("Ticket cost: $15")