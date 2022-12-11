#6 usr input
name = input("What is your name?:")
age = int(input("How old are you?: ")) #注意int()
height = float(input("How tall are you?: "))


age = age + 1 

print("Hello " + name)
print("You are " + str(age) + " years old") #注意str()
print("You are " + str(height)+ "cm tall")