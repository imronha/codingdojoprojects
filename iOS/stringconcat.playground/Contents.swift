//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

print(str)

print("The maximum value \(Int.max)")
print("The minimum value \(Int.min)")

print("The maximum value \(Int32.max)")
print("The minimum value \(Int32.min)")

for i in 1...5 {
    print(i)
}
// loop from 1 to 5 excluding 5
for i in 1..<5 {
    print(i)
}