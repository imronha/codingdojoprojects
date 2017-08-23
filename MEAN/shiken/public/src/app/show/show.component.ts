import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { HttpService } from "./../http.service";

@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent implements OnInit {
  question;
  index;
  constructor(private _httpService: HttpService, private _route: ActivatedRoute) {
      this._route.paramMap
          .switchMap( params => {
              this.index = params.get('fooooool');
              return this._httpService.getSingleQuestion(params.get('fooooool'));
          })
          .subscribe(data => { this.question = data })
  }

  ngOnInit() {
    console.log(this._route)
  }

}
