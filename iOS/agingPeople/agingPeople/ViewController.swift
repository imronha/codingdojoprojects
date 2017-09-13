//
//  ViewController.swift
//  agingPeople
//
//  Created by Imron Hajiahmad on 9/11/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UITableViewDelegate {
    @IBOutlet weak var tableView: UITableView!

    
    var people = ["vinney", "ethan", "andrew", "jose", "jonathan", "jason", "diana", "kalen", "erik", "kat", "ming", "kalinda"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.dataSource = self
        tableView.delegate = self
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    //        print("Section: \(indexPath.section) and Row: \(indexPath.row)")
    //        people.remove(at: indexPath.row)
    //        tableView.reloadData()
    //    }
    //
    
}

extension ViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return people.count
    }
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
//        let cell = [[[UITableViewCell alloc] initWithStyle,:UITableViewCellStyleSubtitle
//            reuseIdentifier:"Mycell"], autorelease];
        cell.textLabel?.text = people[indexPath.row]
        cell.detailTextLabel?.text = String(arc4random_uniform(90)+5)+" Years Old"
        return cell
    }
}
