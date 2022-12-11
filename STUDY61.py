# ************************************************************
# Python daemon threads
# ************************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes
#在后台运行的线程，对程序运行程序不重要 不会等待守护程序线程完成 退出 非守护程序线程通常无法被杀死，在任务完成之前保持活动状态

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer,daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

answer = input("Do you wish to exit?")