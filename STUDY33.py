# delete a file

import os
import shutil

path = "test.txt"
try:
    #os.remove(path) #删除文件
    #os.rmdir(path) #删除空目录
    #shutil.rmtree(path) #删除文件夹并包括下面的文件
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot deleted that using that function")
else:
    print(path + "was deleted")