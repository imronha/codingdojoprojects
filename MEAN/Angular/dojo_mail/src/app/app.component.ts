import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    db = [{
        email: "bil@gates.com",
        importance: true,
        subject: "money",
        content: "hello there"
    },{
        email: "nemo@yas.com",
        importance: true,
        subject: "dogfood",
        content: "woof"
    },{
        email: "yuki@cats.com",
        importance: false,
        subject: "cats",
        content: "hello meow"
    },{
        email: "duh@cook.com",
        importance: true,
        subject: "nope",
        content: "why there"
    }]
}
