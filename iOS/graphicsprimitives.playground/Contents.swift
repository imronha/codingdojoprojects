//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

struct Point{
    var x: Double
    var y: Double
}

struct Line{
    var start: Point
    var end: Point
    
    func returnLength() -> Double {
        let a = (start.x - end.x)
        let b = (start.x - end.x)
        let c = sqrt(pow(a, 2) + pow(b, 2))
        return c
    }
}

let point1 = Point(x:5, y:7)
let point2 = Point(x:6, y:3)
let line = Line(start: point1, end: point2)
line.returnLength()

struct Triangle{
    var Points: [Point]
}