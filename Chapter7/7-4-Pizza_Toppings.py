topping_number = 1
prompt = f"\nEnter topping: "
prompt += "\nEnter 'quit' when finished. "
toppings_list = []
topping = ""

while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"\nAdding topping number {topping_number}: {topping}")
        toppings_list.append(topping.title())
        topping_number += 1

if toppings_list:
    topping_number -= 1
    print(f"\nYour pizza contains the following {topping_number} toppings:")
    print(toppings_list)