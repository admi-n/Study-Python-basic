#32.read file
try:
    with open('1.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :( ")