favorite_numbers = {
    'Shauna': [57,45,32],
    'Alyssa': [7,3,6],
    'Austin': [1,2,3],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")