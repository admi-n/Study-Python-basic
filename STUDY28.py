#31.file detection
import os

p = "C:\\Users\\琚晨阳\\Desktop\\Python"
if os.path.exists(p):
    print("That location exists!")
    if os.path.isfile(p):
        print("That is a file")
    if os.path.isdir(p):
        print("That is a directory")
else:
    print("That location doesn't exist!")