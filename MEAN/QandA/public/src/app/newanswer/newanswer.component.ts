import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-newanswer',
  templateUrl: './newanswer.component.html',
  styleUrls: ['./newanswer.component.scss']
})
export class NewanswerComponent implements OnInit {
  question;
  constructor(private _api: ApiService, private _route: ActivatedRoute) { }

  ngOnInit() {
    this.getQuestion();
  }
  getQuestion(){
      this._route.paramMap
      .switchMap( params => {
          return this._api.getQuestion(params.get('id'));
      })
      .subscribe(data => this.question = data)
  }
}
