#9if statements
#if statement = a block of code that will execute if it's condition is true
#about if elif else https://www.py.cn/jishu/jichu/20693.html

age = int(input("How old are you?: "))

if age ==100: #注意优先原则
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are an child!")
