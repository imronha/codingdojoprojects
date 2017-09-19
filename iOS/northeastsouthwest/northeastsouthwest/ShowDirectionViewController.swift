//
//  ShowDirectionViewController.swift
//  northeastsouthwest
//
//  Created by Imron Hajiahmad on 9/13/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ShowDirectionViewController: UIViewController {
    
    var text: String?
    
    @IBOutlet weak var directionButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        directionButton.titleLabel?.text = text
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    @IBAction func goBackToOneButton(_ sender: Any){
        performSegue(withIdentifier: "unwindSegueToVC1", sender: sender)
    }
}
