#10logical operators

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good tody!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")

if not(temp >= 0 and temp <= 30):
    print("the temperature is good tody!")
    print("go outside!")
elif not(temp < 0 or temp > 30):
    print("the temperature is bad today!")
    print("stay inside!")
