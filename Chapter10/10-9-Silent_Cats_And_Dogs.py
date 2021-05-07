def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)

cats_file = 'cats.txt'
dogs_file = 'dogserr.txt'

read_file(cats_file)
read_file(dogs_file)