#父类子类
#继承
class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("The rabbit is running")
    
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.sleep()
hawk.sleep()
