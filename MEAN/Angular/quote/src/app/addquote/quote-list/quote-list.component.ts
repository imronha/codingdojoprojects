import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-quote-list',
  templateUrl: './quote-list.component.html',
  styleUrls: ['./quote-list.component.css']
})
export class QuoteListComponent implements OnInit {
    @Input() myQuotes;
    @Output() myUpVoteEvent = new EventEmitter();
    @Output() myDownVoteEvent = new EventEmitter();
    @Output() myDeleteEvent = new EventEmitter();

    upVote(quote){
        this.myUpVoteEvent.emit(quote);
    }
    downVote(quote){
        this.myDownVoteEvent.emit(quote);
    }

    delete(quote){
        this.myDeleteEvent.emit(quote);
    }
    constructor() { }

    ngOnInit() {
    }

}
