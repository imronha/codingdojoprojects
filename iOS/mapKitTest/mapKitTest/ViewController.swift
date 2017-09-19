//
//  ViewController.swift
//  mapKitTest
//
//  Created by Imron Hajiahmad on 9/14/17.
//  Copyright © 2017 Imron Hajiahmad. All rights reserved.
//

import UIKit
import MapKit

class ViewController: UIViewController, MKMapViewDelegate, CLLocationManagerDelegate {
    @IBOutlet weak var mapKitView: MKMapView!
    
    let locationManager = CLLocationManager()
    var dragonPin = MKPointAnnotation()

    override func viewDidLoad() {
        super.viewDidLoad()
        mapKitView.delegate = self
        mapKitView.showsScale = true
        mapKitView.showsPointsOfInterest = true
        mapKitView.showsUserLocation = true
        
        locationManager.requestAlwaysAuthorization()
        let dragonCoordinates = CLLocationCoordinate2D(latitude: 40.730872, longitude: -74.003066)
        dragonPin.coordinate = dragonCoordinates
        dragonPin.title = "dragon1"
        mapKitView.addAnnotation(dragonPin)
        
        
    }

    func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) -> MKAnnotationView? {
        if !(annotation is MKPointAnnotation) {
            print("not mkpointannotation")
            return nil
           
        }
        var annotationView = mapKitView.dequeueReusableAnnotationView(withIdentifier: "dragonIdentifier")
        if annotationView == nil{
            annotationView = MKAnnotationView(annotation: annotation, reuseIdentifier: "dragonIdentifier")
            annotationView!.canShowCallout = true
        }else {
            annotationView!.annotation = annotation
        }
        annotationView!.image = UIImage(named: "dragonBlack.png")
        
        let pinImage = UIImage(named: "dragonBlack.png")
        let size = CGSize(width: 50, height: 50)
        UIGraphicsBeginImageContext(size)
        pinImage!.frame.size = CGSize(width: size.width, height: size.height)
        let resizedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        annotationView!.image = resizedImage
        return annotationView
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

