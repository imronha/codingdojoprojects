//
//  ViewController.swift
//  testing1
//
//  Created by Imron Hajiahmad on 9/26/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit

class TableViewController: UITableViewController {
    let data = [["0,0", "0,1", "0,2"], ["1,0", "1,1", "1,2"]]
    var headerTitles = ["section1", "section2"]
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func numberOfSections(in tableView: UITableView) -> Int {
        return data.count
    }
    
    override func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if section < headerTitles.count {
            return headerTitles[section]
        }
        return nil
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return data[section].count
    }

    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "eventCell")
        cell?.textLabel?.text = data[indexPath.section][indexPath.row]
        return cell!
    }
}

