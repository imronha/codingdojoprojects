import { Component } from '@angular/core';
import { Http } from '@angular/http'; //imported here only because were not using a service
import 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  notes = [];
  note = {
      text: "",
  }

  constructor(private _http: Http){
      this.notes = [this._http.get('/').map(data => data.json()).toPromise()];
  }

  addNote(){
      this._http.get('/new', this.note);
      this.note = {
          text:"",
      }
  }
}
