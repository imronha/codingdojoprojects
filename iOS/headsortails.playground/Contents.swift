//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

func tossCoin() -> String {
    print("Tossing a coin!")
    let choice = Int(arc4random_uniform(UInt32(2)))
    if choice == 1{
        return("Heads!")
    } else {
        return("Tails!")
    }

}

tossCoin()

func tossMultipleCoins(tosses: Int) -> Double {
    var heads = 0
    var tails = 0
    for i in 1...tosses{
        if tossCoin() == "Heads!"{
            heads += 1
            print(heads)
        } else {
            tails += 1
            print(tails)
        }
    }
    var total: Double = Double(heads)/Double(tails)
    return(total)
}

tossMultipleCoins(tosses: 5)