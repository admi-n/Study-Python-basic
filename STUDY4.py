#7 math functions
import math

pi = 3.14
print(round(pi))  #round()方法返回浮点数x的四舍五入值。

x = 5.065
y = 6
z = 7
print(round(x,2))
print(round(x,3))
print(round(x,-1))

#在实际使用中发现round函数并不总是如上所说的四舍五入
#print(round(x,3))
#解释:http://www.runoob.com/w3cnote/python-round-func-note.html

print(math.ceil(x)) #大于x的最小整数
print(math.floor(x))#小于x的最大整数
print(abs(x)) #距离0的距离 相当于|x|
print(pow(x,2)) #x的2次幂
print(math.sqrt(x)) #x的平方根

print(max(x,y,z)) #输出最大的数
print(min(x,y,z)) #输出最小的数
 