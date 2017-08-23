import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service'

@Component({
  selector: 'app-newquestion',
  templateUrl: './newquestion.component.html',
  styleUrls: ['./newquestion.component.scss']
})
export class NewquestionComponent implements OnInit {
  question={};
  constructor(private _api: ApiService) { }

  ngOnInit() {
  }
  onSubmit(){
    this._api.createQuestion(this.question)
  }
}
