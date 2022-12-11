#28.string format
#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " +item)
print("The {} jumped over the {}".format("cow",item))
print("The {} jumped over the {}".format(item,item))
print("The {0} jumped over the {1}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))

print("The {animal0} jumped over the {item0}".format(animal0="cow",item0="moon"))
print("The {item0} jumped over the {animal0}".format(animal0="cow",item0="moon"))

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Bro"
print("hello,my name is {} ".format(name))
print("hello,my name is {:10} .Nice to meet you".format(name))
print("hello,my name is {:<10} .Nice to meet you".format(name))
print("hello,my name is {:>10} .Nice to meet you".format(name))
print("hello,my name is {:^10} .Nice to meet you".format(name))

number = 3.1515926
number1 = 1000000
print("The number pi is {:.2f}".format(number))
print("The number pi is {:,.2f}".format(number1))
print("The number is {:b}".format(number1)) #b为2进制
print("The number is {:o}".format(number1)) #o为8进制
print("The number is {:X}".format(number1)) #x为16进制 分大小写
print("The number is {:E}".format(number1)) #e为科学计数法 分大小写