import { Component, OnInit } from '@angular/core';
import { WeatherdataService } from '../weatherdata.service';


@Component({
  selector: 'app-burbank',
  templateUrl: './burbank.component.html',
  styleUrls: ['./burbank.component.css']
})
export class BurbankComponent implements OnInit {
    weather;
    humidity;
    temp;
    maxtemp;
    mintemp;
    status;

      constructor(private _weatherdataService: WeatherdataService) {}

    ngOnInit() {
      this.weather = this._weatherdataService.getWeather('burbank')
      .then(weather => {
          console.log(weather);
          this.humidity = weather.main.humidity;
          this.temp = Math.floor(weather.main.temp * (9/5) - 459.67) + " F";
          this.maxtemp = Math.floor(weather.main.temp_max * (9/5) - 459.67) + " F";
          this.mintemp = Math.floor(weather.main.temp_min * (9/5) - 459.67) + " F";
          this.status = weather.weather[0].main;
      })
  }
}
