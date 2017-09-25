//
//  EditTableViewController.swift
//  myCats
//
//  Created by Imron Hajiahmad on 9/21/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class EditTableViewController: UITableViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    
    
    var delegate: AddCatDelegate?
    
    @IBOutlet weak var nameField: UITextField!
    @IBOutlet weak var colorField: UITextField!
    @IBOutlet weak var treatField: UITextField!
    @IBOutlet weak var photoButton: UIButton!
    
    var name: String?
    var color: String?
    var treat: String?
    var image: UIImage?
    var index: Int?
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        nameField.text = name
        colorField.text = color
        treatField.text = treat
        photoButton.setBackgroundImage(image, for: .normal)
    
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func cancelButtonPressed(_ sender: UIBarButtonItem) {
        dismiss(animated: true, completion: nil)
    }

    @IBAction func doneButtonPressed(_ sender: UIBarButtonItem) {
        let name = nameField.text
        let color = colorField.text
        let treat = treatField.text
        let image = photoButton.backgroundImage(for: .normal)
        delegate?.doneButtonPressed(by: self, name: name!, color: color!, treat: treat!, image: image!, from: index!)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage{
            photoButton.setBackgroundImage(image, for: .normal)
        } else {
            print("Error")
        }
        self.dismiss(animated: true, completion: nil)
        
    }
    
    @IBAction func deleteButtonPressed(_ sender: UITextField) {
    }
    @IBAction func editPhotoButtonPressed(_ sender: UIButton) {
        let image = UIImagePickerController()
        image.delegate = self
        image.sourceType = UIImagePickerControllerSourceType.photoLibrary
        image.allowsEditing = false
        self.present(image, animated: true, completion: nil)
    }
}
