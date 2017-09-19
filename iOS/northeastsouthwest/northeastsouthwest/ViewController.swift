//
//  ViewController.swift
//  northeastsouthwest
//
//  Created by Imron Hajiahmad on 9/13/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func onDirectionButtonPressed(_ sender: UIButton) {
        performSegue(withIdentifier: "showDirectionSegue", sender: sender)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let viewController = segue.destination as! ShowDirectionViewController
        let button = sender as! UIButton
        viewController.text = button.titleLabel!.text
    }
    
    @IBAction func unwindToVC1(segue: UIStoryboardSegue){}
}

