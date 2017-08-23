import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs';

@Injectable()
export class ApiService {
  user = {
      name: "Guest"
  }
  constructor(private _http: Http) { }

  login(user){
      this.user = user;
  }
  getUser(){
      return this.user;
  }
  createQuestion(question){
      return this._http.post('/questions', question)
      .map(data => data.json())
      .toPromise();
  }

  getAllQuestions(){
      return this._http.get('/questions')
      .map(data => data.json())
      .toPromise();
  }

  getQuestion(id){
      return this._http.get('/questions/'+ id)
      .map(data => data.json())
      .toPromise();
  }
}
