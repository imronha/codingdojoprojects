import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map.js';
import 'rxjs/add/operator/toPromise.js';


@Injectable()
export class ScoreService {

  constructor(private _http: Http) { }

  getGithub(username) {
    if (username) {
      return this._http.get(`https://api.github.com/users/${username}`)
      .map( data => data.json() )
      .toPromise();
    }
  }
}
