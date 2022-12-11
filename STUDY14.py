#17tuples

student = ("Bro","21","male")

print(student.count("Bro")) #count() Bro出现的次数
print(student.index("male")) #index() male出现在student的位置
for x in student:
    print(x)
if "Bro" in student:
    print("Bro is here!")