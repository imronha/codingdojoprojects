import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { QuestionlistComponent } from './questionlist/questionlist.component';
import { AddComponent } from './add/add.component';
import { ShowComponent } from './show/show.component';
import { AddanswerComponent } from './addanswer/addanswer.component';

const routes: Routes = [
    { path: '', pathMatch: 'full', component: QuestionlistComponent },
    { path: 'index', component: LoginComponent },
    { path: 'new_question', component: AddComponent },
    { path: 'answer', component: AddanswerComponent },
    { path: 'question/:id', component: ShowComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
