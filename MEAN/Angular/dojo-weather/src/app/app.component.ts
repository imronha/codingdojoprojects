import { Component } from '@angular/core';
import { WeatherdataService } from './weatherdata.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  humidity = null;
  temp = null;
  city = null;
  result;

    constructor(private _weatherdataService: WeatherdataService) {}

    showWeather() {
    this.result = this._weatherdataService.getWeather(this.city)
    if (this.result) {
      this.result.then( (city) => {
        console.log(this.city)
      })
      .catch( (err) => {
        return;
      });
    } else {
      return;
    }
    }


}
