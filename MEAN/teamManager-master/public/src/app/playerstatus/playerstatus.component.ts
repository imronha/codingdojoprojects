import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-playerstatus',
  templateUrl: './playerstatus.component.html',
  styleUrls: ['./playerstatus.component.css']
})
export class PlayerstatusComponent implements OnInit {

  constructor(private router:Router) {
    this.router.navigate(["/status/game/1"])
   }

  

  ngOnInit() {
  }

}
