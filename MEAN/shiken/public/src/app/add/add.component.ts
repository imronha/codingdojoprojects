import { Component, OnInit } from '@angular/core';
import { Question } from './../../../../question';
import { HttpService } from "./../http.service";
import { Router } from '@angular/router';

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit {
    question;
  constructor(private __httpService: HttpService, private router: Router) {
    this.question = new Question();
   }

  ngOnInit() {

  }
  createQuestion(){
    console.log("Calling create question in add.component")
    this.__httpService.createQuestion(this.question);
    this.router.navigate(["/"], function(err){
      if(err){
        console.log("error")
      }
    })


  }

}
