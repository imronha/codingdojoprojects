//
//  AddDelegate.swift
//  contacts
//
//  Created by Imron Hajiahmad on 9/26/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

protocol AddTableViewControllerDelegate: class {
    func saveButtonPressed(firstname: String, lastname: String, number: String, indexpath: NSIndexPath?)
    func cancelButtonPressed()
}
