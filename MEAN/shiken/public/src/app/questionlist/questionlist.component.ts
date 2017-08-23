import { Component, OnInit } from '@angular/core';
import { HttpService } from "./../http.service";

@Component({
  selector: 'app-questionlist',
  templateUrl: './questionlist.component.html',
  styleUrls: ['./questionlist.component.css']
})
export class QuestionlistComponent implements OnInit {
  questions =[];
  constructor(private _httpService: HttpService) {
    this.getQuestions();
  }

  ngOnInit() {
  }
  getQuestions(){
      this._httpService.allQuestions()
      .then( data => { this.questions = data})
      .catch( err => { console.log(err)})
  }

  showQuestion(id){
      console.log("Inside showQuestion from component");
      this._httpService.getSingleQuestion(id);
  }
}
