#move a file

import os

source = "test.txt"
destination = "XXX\\XXX\\XXX.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source + "was moved")
except FileNotFoundError:
    print(source + "was not found")