//
//  AddCatDelegate.swift
//  myCats
//
//  Created by Imron Hajiahmad on 9/21/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit


protocol AddCatDelegate: class {
    func addCatButtonPressed(by controller: AddCatController, name: String, color: String, treat: String, image: UIImage)
    func editButtonPressed(by controller: UICollectionViewCell)
    func doneButtonPressed(by controller: EditTableViewController, name: String, color: String, treat: String, image: UIImage, from indexPath: Int)
}
