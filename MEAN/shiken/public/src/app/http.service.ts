import { Injectable } from '@angular/core';
import { Http } from "@angular/http";
import "rxjs";


@Injectable()
export class HttpService {
    current_user;
    constructor(private _http: Http) {
    }
    login(name){
        this.current_user = name;
    }
    allQuestions(){
        console.log("Getting all questions")
        return this._http.get("/all_questions").map(data => data.json()).toPromise();
    }
    createQuestion(question){
        console.log("Invoked create question in SERVICE", question)
        return this._http.post("/new_question", question).map(data => data.json()).toPromise();
    }

    getSingleQuestion(id){
        console.log("Getting info for question with id", id)
        // return this._http.get("/question/:id", {questionid: id }).map(data => data.json()).toPromise();
    }
}
