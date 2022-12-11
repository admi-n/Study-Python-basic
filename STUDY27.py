#30.exception handing

try:
    number = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = number / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by Zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter onlt numbers")
except Exception as e:
    print(e)
    print("Something went wrong :( ")
finally:
    print("Test")