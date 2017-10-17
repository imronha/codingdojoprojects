//
//  ViewViewController.swift
//  contacts
//
//  Created by Imron Hajiahmad on 9/26/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ViewViewController: UIViewController {
    var delegate: AddTableViewControllerDelegate?
    
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var numberLabel: UILabel!
    
    var contact = Contact()
    
    @IBAction func doneButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.cancelButtonPressed()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nameLabel.text = contact.first! + " " + contact.last!
        numberLabel.text = contact.num!
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}
