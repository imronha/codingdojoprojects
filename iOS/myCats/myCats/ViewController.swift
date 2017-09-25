//
//  ViewController.swift
//  myCats
//
//  Created by Imron Hajiahmad on 9/21/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit
import CoreData

class ViewController: UICollectionViewController, AddCatDelegate {
    var cats = [Cats]()
    
    
    //Communicate with CoreData
    let managedObjectContext = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
    
    override func viewDidLoad() {
        super.viewDidLoad()
        fetchAllItems()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return cats.count
    }
    
    override func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "CatPhotos", for: indexPath) as! CustomCollectionViewCell
        cell.delegate = self
        cell.editButton.setBackgroundImage(UIImage(data: cats[indexPath.row].image! as Data), for: .normal)
        return cell
    }
    
    @IBAction func addButtonPressed(_ sender: UIBarButtonItem) {
        performSegue(withIdentifier: "addSegue", sender: self)
    }
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "addSegue"{
            let add = segue.destination as! AddCatController
            add.delegate = self
        } else if segue.identifier == "editSegue" {
            // Identify the cell as the sender
            let cell = sender as! UICollectionViewCell
            //
            let navi = segue.destination as! UINavigationController
            let edit = navi.topViewController as! EditTableViewController
            edit.delegate = self
            
            let index = cell.tag
            
            edit.name = cats[index].name
            edit.color = cats[index].color
            edit.treat = cats[index].treat
            edit.index = index
            edit.image = UIImage(data: cats[index].image! as Data)
            
        }
    }
    
    // Fetch items from DB
    func fetchAllItems(){
        let request = NSFetchRequest<NSFetchRequestResult>(entityName: "Cats")
        do {
            let results = try managedObjectContext.fetch(request)
            cats = results as! [Cats]
        } catch {
            print("\(error)")
        }
    }
    
    // Without this func, the unwind doesnt know where to go
    @IBAction func unwind(segue: UIStoryboardSegue) {}
    
    // Adding into the DB
    func addCatButtonPressed(by controller: AddCatController, name: String, color: String, treat: String, image: UIImage) {
        // Talking to the entity
        let item = NSEntityDescription.insertNewObject(forEntityName: "Cats", into: managedObjectContext) as! Cats
        item.color = color
        item.name = name
        item.treat = treat
        item.image = UIImagePNGRepresentation(image)! as NSData
        // Appending item into the cats array defined at the top
        cats.append(item)
        
        do{
            // Actually save cats into DB
            try managedObjectContext.save()
        } catch {
            print("\(error)")
        }
        
        collectionView?.reloadData()
    }
    
    func editButtonPressed(by controller: UICollectionViewCell){
        performSegue(withIdentifier: "editSegue", sender: controller)
    }
    
    func doneButtonPressed(by controller: EditTableViewController, name: String, color: String, treat: String, image: UIImage, from indexPath: Int) {
        let item = NSEntityDescription.insertNewObject(forEntityName: "Cats", into: managedObjectContext) as! Cats
        item.color = color
        item.name = name
        item.treat = treat
        item.image = UIImagePNGRepresentation(image)! as NSData
        // Appending item into the cats array defined at the top
        cats[indexPath] = item
        
        do{
            // Actually save cats into DB
            try managedObjectContext.save()
        } catch {
            print("\(error)")
        }
        dismiss(animated: true, completion: nil)
        collectionView?.reloadData()
    }
}

