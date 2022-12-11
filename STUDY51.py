# sort() method   = used with lists
# sort() function = used with iterables

#students = ("Dming","Lihua","S7","Pp","Aaix")

##students.sort(reverse = True)
#sorted_students = sorted(students)

#for i in sorted_students:
#    print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))
            
grade = lambda grades:grades[1]
# students.sort(key=age)                     # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)