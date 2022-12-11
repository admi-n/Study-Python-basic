question = {
    "Who created Python: " : "A",
    "What year was Python created?:" : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"}

options = [["A.Guide van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
           ["A.1989","B,1991","C.2000","D.2016"],
           ["A.Lonely Island","B.Smosh","C.Monty Python","D.SNL"],
           ["A.Ture","B.False","C.sometimes","D.What's Earth"]]

question_num = 1
for key in question:
        print("---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        question_num += 1