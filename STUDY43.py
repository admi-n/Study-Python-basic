#super function
# super() 用于调用父类它返回的临时对象，用于访问父类的方法
#大概意思就是 子从父调用
#        self.length = length
#        self.width = width
#         可以通过父级
#        super().__init__(length,width)


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

#        self.length = length
#        self.width = width

    def area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.length*self.width*self.height
    
square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volume())