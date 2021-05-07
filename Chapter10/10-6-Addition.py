print("Enter two integers to have the sum calculated.")
num_first = input("Enter first integer: ")
num_second = input("Enter second integer: ")

try:
    result = int(num_first) + int(num_second)
except ValueError:
    print("What are you playing at?")
else:
    print(f"The sum of {num_first} and {num_second} is: {result}")