#write a file 

text = "Yooooooooooooo\nThis is some text\nHave a good one!\n"
with open('test.txt','w') as file: #'w'是write的意思会覆盖 还有许多可用参数 比如'a'追加
    file.write(text)
