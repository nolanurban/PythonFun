# testing with file input

location = "C:\\Users\\nolan\\Desktop\\Pythong Testing\\Lorem Ipsem.txt"

with open(location, 'r') as file:
    for line in file:
        print(line, end='')



