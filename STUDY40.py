#多重继承
#一个子类从多个父类派生的概念

class Prey: #prey猎物
    def flee(self):
        print("This animal flees")

class Predator: #predator掠食者
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Finsh(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Finsh()

rabbit.flee()
hawk.hunt()
fish.flee()