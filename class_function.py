#class methods
class Car:

    #Properties of Cars
    color = "White"
    engineHP = "400"
    variant = "Petrol"

    def speed(self, *args, **kwargs):
        speedKMPH = "200"
        print("color of car is "+self.color)
        print("Engine of car is "+self.engineHP)
        print("Variant of car is "+self.variant)
        print("Speed of car is "+speedKMPH)
        print([x*2 for x in args])


#instantiation
car1 = Car()

print(car1.color)
car1.speed(10, 20, 30)