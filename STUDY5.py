#8 string slicing
# [start:stop:step] step表示间隔输出 step=2 间隔2

name = "Helen S7"
first_name = name[0:5] #[:5] 空着表示第一个开始 也就是0
last_name = name[5:8] #[5:] 空着则表示到最后
funky_name = name[0:8:4] 
reversed_name = name[::-1] #颠倒
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name) 

#关于slice()函数https://www.w3school.com.cn/python/ref_func_slice.asp
website = "http://www.oosec.cn"
website1="http://www.hello.oosec.cn"
slice = slice(11,-3)
print(website[slice])
print(website1[slice])
