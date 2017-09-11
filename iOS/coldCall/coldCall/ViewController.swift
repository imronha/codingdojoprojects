//
//  ViewController.swift
//  coldCall
//
//  Created by Imron Hajiahmad on 9/8/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var numLabel: UILabel!
    
    let names = [
        "Imron", "Vinney", "Ethan", "Lorman"
    ]
    var currentName = 0
    var currentNum = 1
    
    override func viewDidLoad() {
        super.viewDidLoad()
        numLabel.isHidden = true
    }

    @IBAction func coldCallPressed(_ sender: UIButton) {
        currentName = Int(arc4random_uniform(UInt32(names.count)))
        currentNum = Int(arc4random_uniform(UInt32(5))+1)
        numLabel.font = numLabel.font.withSize(20)
        numLabel.isHidden = false
        updateUI()
        
    }
    
    func updateUI() {
        nameLabel.text = names[currentName]
        numLabel.text = String(currentNum)
        if currentNum == 1 || currentNum == 2 {
            numLabel.text = String(currentNum)
            numLabel.textColor = UIColor.red
        } else if currentNum == 3 || currentNum == 4 {
            numLabel.text = String(currentNum)
            numLabel.textColor = UIColor.orange
        } else {
            numLabel.text = String(currentNum)
            numLabel.textColor = UIColor.green
        }
    }
}

