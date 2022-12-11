#13netsted loops (嵌套循环)
#nested loops = The "inner loop"will finish all of it's iteraptions迭代 before
#               finishing one iteration of the "outer loop"
rows = int(input("How many rows?: "))
columus = int(input("How many columus?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columus):
        print(symbol,end = "")
    print()
