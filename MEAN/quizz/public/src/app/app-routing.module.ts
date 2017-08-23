import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddComponent } from './add/add.component';
import { ScoresComponent } from './scores/scores.component';
import { QuizComponent } from './quiz/quiz.component';

const routes: Routes = [
    { path: '', pathMatch: 'full', component: ScoresComponent},
    { path: 'add', component: AddComponent },
    { path: 'lets_play', component: QuizComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
