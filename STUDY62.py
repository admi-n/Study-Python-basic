# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
#                   在不同的 CPU 内核上并行运行任务，绕过用于线程的 GIL
#                   多处理 = 更适合 CPU 密集型任务（CPU 使用率高）
#                   多线程 = 更适合 io 绑定任务（等待）

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(100000,))
    b = Process(target=counter, args=(100000,))
    

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()

