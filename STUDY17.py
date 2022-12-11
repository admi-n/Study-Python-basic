#20 indexing
#index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bro Code！"

#if(name[0].islower()): 
#    name = name.capitalize() #将首字母大写

frist_name = name[0:3].upper() #upper()将大写
last_name = name[4:].lower()  #lower()将小写
last_charachter = name[-1]

print(frist_name)
print(last_name)
print(last_charachter)