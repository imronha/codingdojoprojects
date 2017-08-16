import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
    user = {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        street_address: '',
        unit: null,
        city:  '',
        state: '',
    };
    password_confirmation = "";

    registered: boolean;
    users = [];
    onSubmit(){
        this.users.push(this.user);
        this.registered = true;
        console.log(this.users)
    }
    // isRegistered(){
    //     var registered = true;
    // }
    //
}
