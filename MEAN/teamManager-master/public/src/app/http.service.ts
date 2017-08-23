import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class HttpService {

  constructor(private _http: Http) { }
  createPlayer(player) {
    console.log("in the create player service")
    return this._http.post("/createPlayer", player).map(data => data.json()).toPromise();

  }
  allPlayers() {
    return this._http.get("/allPlayers").map(data => data.json()).toPromise();
  }
  updateStatus(status, idx, playerId){
    console.log(`stuff being passed to updateStatus = ${status}, ${idx}, ${playerId}`)
    return this._http.post("/updateStatus", {status:status, idx:idx, playerId:playerId}).map(data=>data.json()).toPromise();
  }
  deletePlayer(playerId){
    console.log("inside delete player service")
    return this._http.post("/deletePlayer", {playerId:playerId}).map(data=>data.json()).toPromise();
  }

}
