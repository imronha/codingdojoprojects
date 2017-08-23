import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { HttpService } from "../../http.service";

@Component({
  selector: 'app-gamelist',
  templateUrl: './gamelist.component.html',
  styleUrls: ['./gamelist.component.css']
})
export class GamelistComponent implements OnInit {
   game = "";
   idx = 0
   players = [];
    constructor(private _route: ActivatedRoute, private _httpService: HttpService) {
      this._route.params.subscribe((param)=>{
        this.game = `game${param.game}`;
        this.idx = param.game - 1;
        console.log("PlayerStatusComponent loaded and url game given is: ", param.game);
      }) 
    }
  ngOnInit() {
    this.getPlayers();
  }
  getPlayers(){
    this._httpService.allPlayers().then( result => { this.players = result}).catch( err => { console.log(err); })
  }
  updateStatus(status, game, playerId){
    this._httpService.updateStatus(status,game,playerId);
    this.getPlayers();
  }
  

}
