import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-addquote',
  templateUrl: './addquote.component.html',
  styleUrls: ['./addquote.component.css']
})
export class AddquoteComponent implements OnInit {
    quotes = []
    quote = {
        content:'',
        author:'',
        rating: 0,
    };
    onSubmit(){
        this.quotes.push(this.quote);
        this.quote= {
            content:'',
            author:'',
            rating: 0,
        }
        console.log(this.quotes);
    }
    upVoted(quote){
        quote.rating +=1;
        console.log(this.quote.rating)
    }
    downVoted(quote){
        quote.rating -=1;
        console.log(this.quote.rating)
    }
    delete(quote){
        const idx = this.quotes.indexOf(quote);
        this.quotes.splice(idx, 1);
    }
    constructor() {
    }

    ngOnInit() {

    }

}
