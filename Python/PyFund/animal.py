
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 150
    def pet(self):
        self.health = self.health + 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Animal, self).__init__()
        self.health = 170
    def fly(self):
        self.health = self.health - 10
        return self

husky = Dog("Bella")
husky.display_health()
husky.walk().walk().walk().run().run().pet().display_health()

zaiross = Dragon("Zaiross")
zaiross.walk().fly().display_health()
