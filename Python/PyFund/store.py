class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
    def display_all(self):
        print "Products: "+ str(self.products)
        print "Location: "+ str(self.location)
        print "Owner: "+ str(self.owner)
        return self
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def remove_product(self, remove_item):
        for i in range(0, len(self.products)-1):
            if self.products[i] == remove_item:
                self.products.pop(i)
        return self
    def inventory(self):
        for i in range(0, len(self.products)-1):
            print str(self.products[i])+" are located in aisle "+str(i)+"."
        return self
frys = Store(["laptops", "pcs", "drones"], "San Jose", "Imron")
frys.add_product("cars").inventory()
