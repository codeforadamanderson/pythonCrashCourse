prompt = "Enter your age (enter 0 to quit): "
age = 100

while age != 0:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Ticket cost: $0")
    elif age < 13:
        print("Ticket cost: $10")
    else:
        print("Ticket cost: $15")