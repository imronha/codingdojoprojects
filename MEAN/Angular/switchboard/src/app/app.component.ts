import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  statuses = [true,true,true,true,true,true,true,true,true,true]
  switched(i){
      this.statuses[i] = !this.statuses[i];
  }
}
