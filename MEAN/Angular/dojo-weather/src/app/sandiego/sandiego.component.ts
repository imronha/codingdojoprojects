import { Component, OnInit } from '@angular/core';
import { WeatherdataService } from '../weatherdata.service';


@Component({
  selector: 'app-sandiego',
  templateUrl: './sandiego.component.html',
  styleUrls: ['./sandiego.component.css']
})
export class SandiegoComponent implements OnInit {

    weather;
    humidity;
    temp;
    maxtemp;
    mintemp;
    status;

      constructor(private _weatherdataService: WeatherdataService) {}

    ngOnInit() {
      this.weather = this._weatherdataService.getWeather('san%20diego')
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
