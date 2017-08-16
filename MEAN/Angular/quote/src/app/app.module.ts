import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { AddquoteComponent } from './addquote/addquote.component';
import { QuoteListComponent } from './addquote/quote-list/quote-list.component';

@NgModule({
  declarations: [
    AppComponent,
    AddquoteComponent,
    QuoteListComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
