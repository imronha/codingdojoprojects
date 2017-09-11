//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

// Print 1-255
for i in 1...255{
    print(i)
}

//Print Odds 1-255
for i in 1...255{
    if i % 2 != 0 {
        print(i)
    }
}

//Swap string for Array neg value
func swapStringForArrayNegVal(arr: [Any]){
    var arr = arr
    for i in 0..<arr.count{
        if let temp = arr[i] as? Int {
            if temp < 0 {
                arr[i] = "Dojo"
            }
        }
    }
}

swapStringForArrayNegVal(arr: [1,2,3,5,-1,-2])


//Print Ints and Sum 1-255

func printIntAndSum(){
    var sum = 0
    for i in 1...255{
        print(i)
        sum += i
        print(sum)
    }
}

printIntAndSum()


func print (num: Int){
    for i in 1...255{
        print(i)
}



