#method overrding

class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a corrot")

rabbit = Rabbit()
rabbit.eat()

#优先选择自己的类