#25.variable scope
#全局变量和局部变量

name = "Bro"
def display_name():
    name = "Code"
    print(name)

display_name()
print(name)