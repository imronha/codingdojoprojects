import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    date = null;
    highlight = null;
    timeChange(timeZone){
        this.date = new Date();
        if (timeZone == 'pst'){
            this.date = new Date();
        }
        if (timeZone == 'mst'){
            this.date.setHours(this.date.getHours()+1);
        }
        if (timeZone == 'cst'){
            this.date.setHours(this.date.getHours()+2);
        }
        if (timeZone == 'est'){
            this.date.setHours(this.date.getHours()+3);
        }
        if (timeZone == 'clear'){
            this.date=null;
        }
        this.highlight = timeZone;
    }
    // user = {
    //     firstName: 'Darth',
    // 	lastName: 'Vader'
    // }
    // amount = 1.20;
    // // today = Date.now();
    // today = Date();
    // // convertMillisecondsToDigitalClock(ms) {
    // //     var hours = Math.floor(ms / 3600000) // 1 Hour = 36000 Milliseconds
    // //     var minutes = Math.floor((ms % 3600000) / 60000) // 1 Minutes = 60000 Milliseconds
    // //     var seconds = Math.floor(((ms % 360000) % 60000) / 1000) // 1 Second = 1000 Milliseconds
    // //         return {
    // //         hours : hours,
    // //         minutes : minutes,
    // //         seconds : seconds,
    // //         clock : hours + ":" + minutes + ":" + seconds
    // //     };
    // // }
}
