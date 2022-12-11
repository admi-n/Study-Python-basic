class Car:

    def __init__(self,make,model,year,color):
        self.makee = make
        self.modell = model
        self.yearr = year
        self.colorr = color
        
    def drive(self):
        print("This " + self.modell+ " is driving")
    def stop(self):
        print("This "+ self.modell+ " is stoping")