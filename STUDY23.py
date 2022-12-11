#26.args
# *args = parameter that will pack all arguments into a tuple
#          useful so that a function can accept a varying amount of arguments

#def add(num1,num2):
#    sum = num1 + num2
#    return sum

#print(add(1,2))

def add(*n):
    sum = 0
    n = list(n)
    n[0] = 0
    for i in n:
        sum += i
    return sum


print(add(1,2,3,5))

