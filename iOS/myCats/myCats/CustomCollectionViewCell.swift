//
//  CustomCollectionViewCell.swift
//  myCats
//
//  Created by Imron Hajiahmad on 9/21/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class CustomCollectionViewCell: UICollectionViewCell {
    
    var delegate: ViewController?
    
    @IBOutlet weak var editButton: UIButton!
    
    @IBAction func editButtonPressed(_ sender: UIButton) {
        print("Edit Pressed")
        delegate?.editButtonPressed(by: self)
    }
}
