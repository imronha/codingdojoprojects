import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map.js';
import 'rxjs/add/operator/toPromise.js';

@Injectable()
export class WeatherdataService {

    constructor(private _http: Http) { }

    getWeather(city) {
      if (city) {
        return this._http.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&APPID=7bd200e5b916a2cf609349d883f47d92`)
        .map( data => data.json()).toPromise();
      }
    }
}
