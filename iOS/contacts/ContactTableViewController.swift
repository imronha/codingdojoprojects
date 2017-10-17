//
//  ContactTableViewController.swift
//  contacts
//
//  Created by Imron Hajiahmad on 9/26/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit
import CoreData

class ContactTableViewController: UITableViewController, AddTableViewControllerDelegate {
    
    var contacts = [Contact]()
    
    // CoreData
    let MOC = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
    func saveDB(){
        if MOC.hasChanges {
            do { try MOC.save() }
            catch { print(error) }
        }
    }
    func fetchData(){
        let request:NSFetchRequest<Contact> = Contact.fetchRequest()
        do {
            contacts = try MOC.fetch(request)
        } catch {
            print(error)
        }
    }
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        fetchData()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "addContact"{
            let navi = segue.destination as! UINavigationController
            let controller = navi.topViewController as! AddTableViewController
            controller.delegate = self
        } else if segue.identifier == "editContact"{
            let navi = segue.destination as! UINavigationController
            let controller = navi.topViewController as! AddTableViewController
            controller.delegate = self
            if let ip = sender as? NSIndexPath{
                controller.indexPath = ip
                controller.first = contacts[ip.row].first
                controller.last = contacts[ip.row].last
                controller.number = contacts[ip.row].num
                navigationItem.title = "Edit Contact"
            }
        } else if segue.identifier == "viewContact"{
            let navi = segue.destination as! UINavigationController
            let controller = navi.topViewController as! ViewViewController
            controller.delegate = self
            if let ip = sender as? NSIndexPath{
                controller.contact = contacts[ip.row]
                controller.navigationItem.title = contacts[ip.row].first
            }
            
        }
    }
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return contacts.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "contactCell", for: indexPath)
        cell.textLabel?.text = contacts[indexPath.row].first! + " " + contacts[indexPath.row].last!
        cell.detailTextLabel?.text = contacts[indexPath.row].num
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let actionMenu = UIAlertController(title: nil, message: nil, preferredStyle: .actionSheet)
        
        let editAction = UIAlertAction(title: "Edit", style: .default, handler: {
            (alert: UIAlertAction!) -> Void in
            self.performSegue(withIdentifier: "editContact", sender: indexPath)
        })
        
        let deleteAction = UIAlertAction(title: "Delete", style: .default, handler: {
            (alert: UIAlertAction!) -> Void in
            self.MOC.delete(self.contacts[indexPath.row])
            self.saveDB()
            self.fetchData()
            self.tableView.reloadData()
        })
        let viewAction = UIAlertAction(title: "View", style: .default, handler: {
            (alert: UIAlertAction!) -> Void in
            self.performSegue(withIdentifier: "viewContact", sender: indexPath)
        })
        
        let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        
        actionMenu.addAction(editAction)
        actionMenu.addAction(deleteAction)
        actionMenu.addAction(viewAction)
        actionMenu.addAction(cancelAction)
        
        self.present(actionMenu, animated: true, completion: nil)
        
    }
    
    
    func saveButtonPressed(firstname: String, lastname: String, number: String, indexpath: NSIndexPath?) {
        if let ip = indexpath{
            let editperson = contacts[ip.row]
            editperson.first = firstname
            editperson.last = lastname
            editperson.num = number
        }else {
            let newPerson = NSEntityDescription.insertNewObject(forEntityName: "Contact", into: MOC) as! Contact
            newPerson.first = firstname
            newPerson.last = lastname
            newPerson.num = number
            
        }
        saveDB()
        fetchData()
        tableView.reloadData()
        dismiss(animated: true, completion: nil)
    }
    
    func cancelButtonPressed() {
        dismiss(animated: true, completion: nil)
    }
}
