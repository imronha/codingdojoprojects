import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    colorArray =[];

    pickColors(){
        for(var i =0; i<10; i++){
            var color = "#"+Math.floor(Math.random()*9)+Math.floor(Math.random()*9)+Math.floor(Math.random()*9)+Math.floor(Math.random()*9)+Math.floor(Math.random()*9)+Math.floor(Math.random()*9);
            this.colorArray.push(color);
        }
    };
    ngOnInit() {
        this.pickColors();
    }
}
