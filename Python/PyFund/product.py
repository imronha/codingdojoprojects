class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        # self.cost = cost
        self.status = "For sale"
        # self.display_all()
    def tax(self):
        taxes = self.price*(0.15)
        self.price = taxes + self.price
        return self
        # print self.price
        # print total_price
    def display_all(self):
        print "Price: "+ str(self.price)
        print "Name: "+ str(self.name)
        print "Weight: "+ str(self.weight)
        print "Brand: "+ str(self.brand)
        print "Status: "+ str(self.status)
    def sell(self):
        self.status = "Sold"
        return self
    def returned(self, reason, condition):
        if reason == "defective":
            self.price = 0
            self.status = "Defective"
            return self
        elif condition == "opened":
            self.status = "Used. Returned because: "+str(reason)
            self.price = "$"+str((self.price - (self.price*0.20)))+"  (A 20 percent discount was applied!)"
            return self


product1 = Product(40, "Echo dot", 1, "Amazon")
product1.returned("defective", "opened").display_all()
