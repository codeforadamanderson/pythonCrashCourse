def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} does not exist.")
    else:
        print(contents)

cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

read_file(cats_file)
read_file(dogs_file)