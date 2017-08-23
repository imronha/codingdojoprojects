import { Component, OnInit } from '@angular/core';
import { Player } from "../../player";
import { HttpService } from "../../http.service";
import { Router } from '@angular/router';


@Component({
  selector: 'app-playeradd',
  templateUrl: './playeradd.component.html',
  styleUrls: ['./playeradd.component.css']
})
export class PlayeraddComponent implements OnInit {
    player;
  constructor(private __httpService: HttpService, private router: Router) {
    this.player = new Player();
   }

  ngOnInit() {
    
  }
  createPlayer(){
    console.log("calling create player in component")
    this.__httpService.createPlayer(this.player);
    console.log("now trying square brackets really")
    this.router.navigate(["/players/list"], function(err){
      if(err){
        console.log("error in router navigatebyurl")
      }
      else{
        console.log("navigatebyurl succeeded")
      }
    })
    

  }

}
