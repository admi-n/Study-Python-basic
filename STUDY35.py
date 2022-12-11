#quiz game
#----------------------------------------------
def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("---------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(question.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

#----------------------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("correct!")
        return 1
    else:
        print("error!")
        return 0   
#----------------------------------------------
def display_score(correct_guesses,guesses):
    print("--------")
    print("results")
    print("--------")
    print("正确答案是: ",end="")
    for i in question:
        print(question.get(i),end=" ")
    print()

    print("你的答案是: ",end="")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(question))*100)
    print("你的成绩比是: "+str(score)+"%")
#----------------------------------------------
def play_again():
    response = input("你想要在玩一次吗?: (YES/NO)")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
    
#----------------------------------------------

question = {
    "Who created Python: " : "A",
    "What year was Python created?:" : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"}

options = [["A.Guide van Rossum","B.Elon Musk","C.Bill Gates","D.Mark Zuckerburg"],
           ["A.1989","B,1991","C.2000","D.2016"],
           ["A.Lonely Island","B.Smosh","C.Monty Python","D.SNL"],
           ["A.Ture","B.False","C.sometimes","D.What's Earth"]]

new_game()

while play_again():
    new_game()
print("游戏愉快！下次再玩！")