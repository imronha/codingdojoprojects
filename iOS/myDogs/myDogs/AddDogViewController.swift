//
//  AddDogViewController.swift
//  myDogs
//
//  Created by Imron Hajiahmad on 9/18/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class AddDogViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var colorTextField: UITextField!
    @IBOutlet weak var treatTextField: UITextField!
    var delegate: DogDelegate?

    @IBOutlet weak var dogPhoto: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    
    @IBAction func addPhotoPressed(_ sender: UIButton) {
        let image = UIImagePickerController()
        image.delegate = self
        
        image.sourceType = UIImagePickerControllerSourceType.photoLibrary
        image.allowsEditing = false
        
        self.present(image, animated: true){
            
        }
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        if let image = info[UIImagePickerControllerOriginalImage] as? UIImage {
            dogPhoto.setBackgroundImage(image, for: .normal)
            dogPhoto.setTitle("", for: .normal)
        } else {
            print("Error")
        }
        dismiss(animated: true, completion: nil)
    }
    
}
