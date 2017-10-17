//
//  AddTableViewController.swift
//  contacts
//
//  Created by Imron Hajiahmad on 9/26/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class AddTableViewController: UITableViewController {
    
    var delegate: AddTableViewControllerDelegate?
    
    var first: String?
    var last: String?
    var number: String?
    var indexPath: NSIndexPath?

    @IBOutlet weak var firstNameTextField: UITextField!
    @IBOutlet weak var lastNameTextField: UITextField!
    @IBOutlet weak var numberTextField: UITextField!
    
    @IBAction func saveButtonPressed(_ sender: UIBarButtonItem) {
        let first = firstNameTextField.text!
        let last = lastNameTextField.text!
        let number = numberTextField.text!
        delegate?.saveButtonPressed(firstname: first, lastname: last, number: number, indexpath: indexPath)
        
    }
    
    @IBAction func cancelButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.cancelButtonPressed()
    }
    
    
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if let _ = indexPath{
            firstNameTextField.text = first
            lastNameTextField.text = last
            numberTextField.text = number
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }



}
