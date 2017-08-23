import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { AddComponent } from './add/add.component';
import { QuestionlistComponent } from './questionlist/questionlist.component';
import { HttpService } from "./http.service";
import { AddanswerComponent } from './addanswer/addanswer.component';
import { ShowComponent } from './show/show.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    AddComponent,
    QuestionlistComponent,
    AddanswerComponent,
    ShowComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }
