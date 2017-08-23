import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
    products = []
    product = {
        title:'',
        price: Number,
        image: '',
    };
    onSubmit(){
        this.products.push(this.product);
        this.product= {
            title:'',
            price:null,
            image: '',
        }
        console.log(this.products);
    }
    // upVoted(quote){
    //     quote.rating +=1;
    //     console.log(this.quote.rating)
    // }
    // downVoted(quote){
    //     quote.rating -=1;
    //     console.log(this.quote.rating)
    // }
    // delete(quote){
    //     const idx = this.quotes.indexOf(quote);
    //     this.quotes.splice(idx, 1);
    // }
  constructor() { }

  ngOnInit() {
  }

}
