import { Component, OnInit } from '@angular/core';
import { HttpService } from "../../http.service";

@Component({
  selector: 'app-playerlist',
  templateUrl: './playerlist.component.html',
  styleUrls: ['./playerlist.component.css']
})
export class PlayerlistComponent implements OnInit {
   players = [];
  constructor(private _httpService: HttpService) {
    this.getPlayers();
   }

  ngOnInit() {
  }
    getPlayers(){
    this._httpService.allPlayers().then( result => { this.players = result}).catch( err => { console.log(err); })
  }
  deletePlayer(playerId){
    console.log("inside delete player")
    this._httpService.deletePlayer(playerId);
    this.getPlayers();
  }


}
