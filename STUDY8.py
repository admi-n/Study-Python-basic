#11 while loops
# while loops = a statement that will execute it's block of code
#               as long as it's condition remains true

#while 1==1:
#   print("Help! l'm stuck in a loop!")
name = ""
while len(name) ==0:
    name = input("Enter your name: ")
print("hello "+ name)

name = None
while not name:
    name = input("Enter your name: ")
print("hello " + name)