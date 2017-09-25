//
//  AddCatController.swift
//  myCats
//
//  Created by Imron Hajiahmad on 9/21/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class AddCatController: UITableViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    var delegate: AddCatDelegate?
    
    @IBOutlet weak var photButton: UIButton!
    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var colorField: UITextField!
    @IBOutlet weak var treatField: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    @IBAction func photoButtonPressed(_ sender: UIButton) {
        let image = UIImagePickerController()
        image.delegate = self
        image.sourceType = UIImagePickerControllerSourceType.photoLibrary
        image.allowsEditing = false
        self.present(image, animated: true, completion: nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage{
            photButton.setBackgroundImage(image, for: .normal)
        } else {
            print("Error")
        }
        self.dismiss(animated: true, completion: nil)
        
    }
    
    @IBAction func addCatButtonPressed(_ sender: UIButton) {
        delegate?.addCatButtonPressed(by: self, name: nameField.text!, color: colorField.text!, treat: treatField.text!, image: photButton.backgroundImage(for: .normal)!)
        
        // Unwind after adding cat
        performSegue(withIdentifier: "unwindSegue", sender: self)
    }
    
}
