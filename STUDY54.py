# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#            将函数应用于可迭代对象，并将其减少为单个累积值。
#            对前两个元素执行函数并重复处理，直到剩下 1 个值
# reduce(function, iterable可迭代)
#参数
#function -- 函数，有两个参数
#iterable -- 可迭代对象
#initializer -- 可选，初始参数

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)

#eg：
#def add(x, y) :            # 两数相加
#    return x + y
#sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
#sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
#print(sum1)
#print(sum2)