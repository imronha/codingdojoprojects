import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NewquestionComponent } from './newquestion/newquestion.component'
import { ShowquestionComponent } from './showquestion/showquestion.component'
import { NewanswerComponent } from './newanswer/newanswer.component'

const routes: Routes = [
    { path: '', pathMatch: 'full', component: LoginComponent },
    { path: 'dashboard', pathMatch: 'full', component: DashboardComponent },
    { path: 'new_question', pathMatch: 'full', component: NewquestionComponent },
    { path: 'question/:id', pathMatch: 'full', component: ShowquestionComponent },
    { path: 'question/:id/new_answer', pathMatch: 'full', component: NewanswerComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
