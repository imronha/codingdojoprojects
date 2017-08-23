import { Component, OnInit } from '@angular/core';
import { ApiService } from './../api.service';
import { Router, ActivatedRoute } from '@angular/router';
import 'rxjs';

@Component({
  selector: 'app-showquestion',
  templateUrl: './showquestion.component.html',
  styleUrls: ['./showquestion.component.scss']
})
export class ShowquestionComponent implements OnInit {
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
