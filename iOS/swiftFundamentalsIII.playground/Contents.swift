//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"


//Write a program that adds the numbers 1-255 to an array
//Swap two random values in the array
//Hint: you can use the arc4random_uniform(UInt32) function to get a random number from 0 to the number passed in. The arc4random_uniform function takes in one parameter that is of the UInt32 type and returns a random number that is of the UInt32 type. How can you deal with this using your knowledge of types?
//Now write the code that swaps random values 100 times (You've created a "Shuffle"!)
//Remove the value "42" from the array and Print "We found the answer to the Ultimate Question of Life, the Universe, and Everything at index __" and print the index of where "42" was before you removed it.

var array = [Int]()
for i in 1...255{
    array.append(i)
}

var rand1 = Int(arc4random_uniform(UInt32(array.count)))
var rand2 = Int(arc4random_uniform(UInt32(array.count)))

if rand1 != rand2 {
    swap(&array[rand1], &array[rand2])
}


for i in 1...100 {
    var rand1 = Int(arc4random_uniform(UInt32(array.count)))
    var rand2 = Int(arc4random_uniform(UInt32(array.count)))
    
    if rand1 != rand2 {
        swap(&array[rand1], &array[rand2])
    }
    
}

for i in 0..<array.count {
    
    if(array[i] == 45){
        
        array.remove(at: i)
        
        print("We found the answer to the Ultimate Question of Life, the Universe, and Everything at index \(i)")
        
        break
    }
    
}