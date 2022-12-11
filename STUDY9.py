#12for loops
#for loop = a statement that will execute it's block of code
#           a limited amount of times
#
#           while loop = unlimited
#           for loop = limited

#for i in range(10): #rang(10) 从0开始10个数 0~9
#    print(i + 1) 
#for i in range(50,100+1):  #rang(50,100) 从50开始到99   
#    print(i) 

#for i in range(50,100+1,2): #从50开始依次加2到100
#    print(i)

#for i in "Bro Code":
#   print(i)

import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
