filename = 'movie_titles.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    line = line.replace('Return', 'Revenge')
    print(line)