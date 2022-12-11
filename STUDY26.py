#29.random numbers
import random

x = random.randint(1,6) #随机生成1~6的随机整数
y = random.random() #随机0~1的任何数字
mylist = ['rock','paper','scissors']
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q",'K']
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)