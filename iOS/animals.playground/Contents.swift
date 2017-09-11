//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

class Animal {
    var name: String
    var health: Int = 100
    init (name: String) {
        self.name = name
    }
    func displayHealth(){
        print(name, "has", health, "health.")
    }
}

class Cat: Animal {
    override init(name: String){
        super.init(name: name)
        self.health = 150
    }
    func growl() {
        print(name, "Rawrd!")
    }
    func run(){
        print(name, "Ran! Lost 10 health.")
        if self.health > 10{
            self.health -= 10
        } else{
            self.health = 1
        }
        
    }
}

class Lion: Cat {
    override init(name: String){
        super.init(name: name)
        self.health = 200
    }
    
    override func growl() {
        print(name, "ROARED!! I am the king of the jungle")
    }
}

class Cheetah: Cat{
    override init(name: String){
        super.init(name: name)
        self.health = 200
    }
    
    override func run() {
        print("Running fast! Lost 50 health")
        self.health -= 50
    }
    
    func sleep(){
        print(name, "went to sleep! Regained 50 health")
        self.health += 50
    }
    
}
var yuki = Cat(name: "Yuki")
yuki.displayHealth()
yuki.growl()
yuki.run()
yuki.displayHealth()

var simba = Lion(name: "Simba")
simba.displayHealth()
simba.growl()

//var ming = Lion(name: "Ming")
//ming.displayHealth()
//ming.run()
//ming.run()
//ming.displayHealth()
//ming.run()
//ming.run()
//ming.run()
//ming.run()
//ming.displayHealth()
