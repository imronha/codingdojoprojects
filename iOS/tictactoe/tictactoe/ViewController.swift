//
//  ViewController.swift
//  tictactoe
//
//  Created by Imron Hajiahmad on 9/8/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
//    @IBOutlet weak var button1: UIButton!
//    @IBOutlet weak var button2: UIButton!
//    @IBOutlet weak var button3: UIButton!
//    @IBOutlet weak var button4: UIButton!
//    @IBOutlet weak var button5: UIButton!
//    @IBOutlet weak var button6: UIButton!
//    @IBOutlet weak var button7: UIButton!
//    @IBOutlet weak var button8: UIButton!
//    @IBOutlet weak var button9: UIButton!
//    
//
    
    @IBOutlet var buttons: [UIButton]!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        reset()
        // Do any additional setup after loading the view, typically from a nib.
    }
    var currentUser = true
    
    @IBAction func buttonPressed(_ sender: UIButton) {
        if currentUser == true && sender.backgroundColor == UIColor.black {
            sender.backgroundColor = UIColor.red
            if checkIfWon(tag: sender.tag, color: UIColor.red) {
                
            }
            currentUser = !currentUser
        }
        if currentUser == false && sender.backgroundColor == UIColor.black {
            sender.backgroundColor = UIColor.blue
            currentUser = !currentUser
        }
        
    }
    
    func checkIfWon(tag: Int, color: UIColor) -> Bool {
        switch tag {
        case 1 :
            if tag[1].backgroundColor == color{
                return true
            }
        default:
            return false
        }
        return false
    }
    
    func reset(){
        for button in buttons{
            button.backgroundColor = UIColor.black
            
        }
    }
    
    @IBAction func resetPressed(_ sender: UIButton) {
        currentUser = true
        reset()
    }

//
//    @IBAction func button1pressed(_ sender: UIButton) {
//        if currentUser == true && button1.backgroundColor == UIColor.black {
//            button1.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button1.backgroundColor == UIColor.black {
//            button1.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    @IBAction func button2pressed(_ sender: UIButton) {
//        if currentUser == true && button2.backgroundColor == UIColor.black {
//            button2.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button2.backgroundColor == UIColor.black {
//            button2.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//
//    @IBAction func button3pressed(_ sender: UIButton) {
//        if currentUser == true && button3.backgroundColor == UIColor.black {
//            button3.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button3.backgroundColor == UIColor.black {
//            button3.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//
//    @IBAction func button4pressed(_ sender: UIButton) {
//        if currentUser == true && button4.backgroundColor == UIColor.black {
//            button4.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button4.backgroundColor == UIColor.black {
//            button4.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    @IBAction func button5pressed(_ sender: UIButton) {
//        if currentUser == true && button5.backgroundColor == UIColor.black {
//            button5.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button5.backgroundColor == UIColor.black {
//            button5.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    @IBAction func button6pressed(_ sender: UIButton) {
//        if currentUser == true && button6.backgroundColor == UIColor.black {
//            button6.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button6.backgroundColor == UIColor.black {
//            button6.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    @IBAction func button7pressed(_ sender: UIButton) {
//        if currentUser == true && button7.backgroundColor == UIColor.black {
//            button7.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button7.backgroundColor == UIColor.black {
//            button7.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    @IBAction func button8pressed(_ sender: UIButton) {
//        if currentUser == true && button8.backgroundColor == UIColor.black {
//            button8.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button8.backgroundColor == UIColor.black {
//            button8.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    @IBAction func button9pressed(_ sender: UIButton) {
//        if currentUser == true && button9.backgroundColor == UIColor.black {
//            button9.backgroundColor = UIColor.red
//            currentUser = !currentUser
//        }
//        if currentUser == false && button9.backgroundColor == UIColor.black {
//            button9.backgroundColor = UIColor.blue
//            currentUser = !currentUser
//        }
//    }
//    
//    
    
}





//import UIKit
//
//class ViewController: UIViewController {
//    
//    @IBOutlet weak var blockOne: UIButton!
//    
//    @IBOutlet weak var blockTwo: UIButton!
//    
//    @IBOutlet weak var blockThree: UIButton!
//    
//    @IBOutlet weak var blockFour: UIButton!
//    
//    @IBOutlet weak var blockFive: UIButton!
//    
//    @IBOutlet weak var blockSix: UIButton!
//    
//    @IBOutlet weak var blockSeven: UIButton!
//    
//    @IBOutlet weak var blockEight: UIButton!
//    
//    @IBOutlet weak var blockNine: UIButton!
//    
//    
//    @IBOutlet weak var winLabel: UILabel!
//    
//    var pressedBlocks = [Int]()
//    var colors = ["grey","grey","grey","grey","grey","grey","grey","grey","grey"]
//    
//    var b1 = false
//    var b2 = false
//    var b3 = false
//    var b4 = false
//    var b5 = false
//    var b6 = false
//    var b7 = false
//    var b8 = false
//    var b9 = false
//    var turn = 1;
//    
//    @IBAction func squarePressed(_ sender: UIButton) {
//        if notPressed(arr: pressedBlocks,spot: sender.tag){
//            pressedBlocks.append(sender.tag)
//            if turn == 1{
//                sender.backgroundColor = UIColor.red
//                colors[sender.tag - 1] = "red"
//                turn = 2
//                checkGame(position: sender.tag, color: "red")
//            }else{
//                sender.backgroundColor = UIColor.blue
//                colors[sender.tag - 1] = "blue"
//                turn = 1
//                checkGame(position: sender.tag, color: "blue")
//            }
//        }
//        
//        
//    }
//    
//    
//    
//    
//    func notPressed(arr: [Int], spot: Int) -> Bool{
//        for i in 0..<arr.count {
//            if arr[i] == spot{
//                return false
//            }
//        }
//        return true;
//    }
//    
//    func checkGame(position: Int, color: String){
//        
//        //check from bottom to top
//        if position - 6 >= 1 && position - 6 <= 3{
//            if colors[position - 1 - 3] == color && colors[position - 1 - 6] == color{
//                gameOver(color: color)
//            }
//        }
//        //checks from top to bottom
//        if position + 6 >= 7 && position + 6 <= 9{
//            if colors[position - 1 + 3] == color && colors[position - 1 + 6] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks from left to right
//        if (position + 2) % 3 == 0{
//            if colors[position - 1 + 2] == color && colors[position - 1 + 1] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks from right to left
//        if (position - 2) == 1 || (position - 2) == 4 || (position - 2) == 7 {
//            if colors[position - 1 - 2] == color && colors[position - 1 - 1] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks above and below
//        if (position - 3) >= 1 && (position - 3) <= 3{
//            if colors[position - 1 - 3] == color && colors[position - 1 + 3] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks diagonal bottom to top-right
//        if (position - 4) == 3{
//            if colors[position - 1 - 2] == color && colors[position - 1 - 4] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks diagonal top to bottom-left
//        if (position + 4) == 7{
//            if colors[position - 1 + 2] == color && colors[position - 1 + 4] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks diagonal top to bottom-right
//        if (position + 8) == 9{
//            if colors[position - 1 + 4] == color && colors[position - 1 + 8] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks diagonal bottom to top-left
//        if (position - 8) == 1{
//            if colors[position - 1 - 4] == color && colors[position - 1 - 8] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        //checks diagonal middle in all directions
//        if (position - 2) == 3{
//            if colors[position - 1 - 2] == color && colors[position - 1 + 2] == color{
//                gameOver(color: color)
//            }else if colors[position - 1 - 4] == color && colors[position - 1 - 2] == color{
//                gameOver(color: color)
//            }
//        }
//        
//        
//    }
//    
//    
//    
//    func gameOver(color:String){
//        winLabel.text = "\(color) wins"
//        winLabel.isHidden = false
//    }
//    
//    
//    
//    override func viewDidLoad() {
//        super.viewDidLoad()
//        
//        winLabel.isHidden = true
//        
//    }
//    
//    
//    @IBAction func resetGame(_ sender: UIButton) {
//        winLabel.isHidden = true
//        colors = ["grey","grey","grey","grey","grey","grey","grey","grey","grey"]
//        pressedBlocks = [Int]()
//        turn = 1
//        blockOne.backgroundColor = UIColor.gray
//        blockTwo.backgroundColor = UIColor.gray
//        blockThree.backgroundColor = UIColor.gray
//        blockFour.backgroundColor = UIColor.gray
//        blockFive.backgroundColor = UIColor.gray
//        blockSix.backgroundColor = UIColor.gray
//        blockSeven.backgroundColor = UIColor.gray
//        blockEight.backgroundColor = UIColor.gray
//        blockNine.backgroundColor = UIColor.gray
//        
//        
//    }
//    
//    
//    override func didReceiveMemoryWarning() {
//        super.didReceiveMemoryWarning()
//        
//    }
//    
//    
//}


