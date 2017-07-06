# Assignment: Car
# Create a class called  Car. In the__init__(), allow the user to specify the following
# attributes: price, speed, fuel, mileage. If the price is greater than 10,000,
# set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car. In the class have a method called
# display_all() that returns all the information about the car as a string. In
# your __init__(), call this display_all() method to display information about the car
# once the attributes have been defined.
class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print self
        print "Price: "+str(self.price)
        print "Speed: "+str(self.speed)+" mph"
        print "Fuel: "+str(self.fuel)
        print "Mileage: "+str(self.mileage)+" mpg"
        print "Tax: "+str(self.tax)

lambo = Car(200000, 300, "Empty", 10)
lambo.display_all()
civic = Car(25000, 130, "Full", 35)
civic.display_all()
prius = Car(25000, 120, "Full", 50)
prius.display_all()
hummer = Car(35000, 150, "Empty", 15)
hummer.display_all()
camaro = Car(60000, 200, "Empty", 19)
camaro.display_all()
tesla = Car(80000, 200, "Full", 89)
tesla.display_all()
