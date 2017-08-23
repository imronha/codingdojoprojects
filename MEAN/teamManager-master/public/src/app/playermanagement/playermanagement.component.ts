import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-playermanagement',
  templateUrl: './playermanagement.component.html',
  styleUrls: ['./playermanagement.component.css']
})
export class PlayermanagementComponent implements OnInit {

  constructor(private router:Router) {
    this.router.navigate(["/players/list"]);
   }
   
  ngOnInit() {
  }

}
