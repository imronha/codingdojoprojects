//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

struct Card {
    var color: String
    var roll: Int
//    init(color: String) {
//        if color == "Blue"{
//            roll = Int(arc4random_uniform(2))+1
//        }else if color == "Red"{
//            roll = Int(arc4random_uniform(2))+3
//        }else if color == "Green"{
//            roll = Int(arc4random_uniform(2))+4
//        }
//    }
    func show(){
        print(color, roll)
    }
}

var card1: Card = Card(color: "Red", roll: 1)

class Deck {
    var cards: [Card]
    init () {
    cards = [Card]()
        for _ in 1...10 {
            var randomint: Int = Int(arc4random_uniform(2)+1)
            cards.append(Card(color: "Blue", roll: randomint))
            randomint = Int(arc4random_uniform(2)+3)
            cards.append(Card(color: "Red", roll: randomint))
            randomint = Int(arc4random_uniform(2)+4)
            cards.append(Card(color: "Green", roll: randomint))
        }
    }
    func dealcard() -> Card {
        let top: Card? = cards.remove(at: 0)
        if let random = top {
            return random
        }else {
            return Card(color: "", roll: 0)
        }
    }
    func isEmpty() -> Bool {
        return cards.count == 0
    }
    
    func shuffle(){
        print("Shuffling deck")
        var first: Int
        var second: Int
        var temp: Card
        for _ in 1...cards.count {
            first = Int(arc4random_uniform(UInt32(cards.count)))
            second = Int(arc4random_uniform(UInt32(cards.count)))
            temp = cards[first]
            cards[first] = cards[second]
            cards[second] = temp
        }
    }
    func show(){
        print("Current cards in deck:")
        for card in self.cards{
            card.show()
        }
    }
}

class Player{
    var name: String
    var hand: [Card]
    init (name: String){
        self.name =  name
        hand = [Card]()
    }
    
    func draw(deck: Deck) -> Card {
        let top = deck.dealcard()
        if top.color != "" && top.roll != 0{
            hand.append(top)
        }
        return top
    }
    func rollDice() -> Int {
        return Int(arc4random_uniform(UInt32(6)+1))
    }
    
    func matchingCards(colour: String, roll: Int) -> Int{
        var count = 0
        for i in 1...hand.count{
            if hand[i].color == colour && hand[i].roll == roll {
                count += 1
            }
        }
        return count
    }
}

var deck: Deck = Deck()
deck.show()
var player: Player = Player(name: "Imron")
deck.shuffle()
deck.show()
