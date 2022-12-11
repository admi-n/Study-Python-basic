#27.kwargs
#
#

#def hello(**kwargs):
#    print("Hello " + kwargs['first'] + " " + kwargs['last'])
#hello(first="Bro",middle="Dudo",last="Code")

def hello(**kwargs):
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")
hello(title="Mr.",first="Bro",middle="Dudo",last="Code")