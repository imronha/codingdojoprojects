import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { WeatherdataService } from './weatherdata.service';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { BurbankComponent } from './burbank/burbank.component';
import { DavisComponent } from './davis/davis.component';
import { SandiegoComponent } from './sandiego/sandiego.component';
import { NewyorkComponent } from './newyork/newyork.component';
import { TokyoComponent } from './tokyo/tokyo.component';
import { PortlandComponent } from './portland/portland.component';
import { LinksComponent } from './links/links.component';

import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  // { path: '', pathMatch: 'full', component: LinksComponent },
  { path: 'burbank', component: BurbankComponent },
  { path: 'davis', component: DavisComponent },
  { path: 'newyork', component: NewyorkComponent },
  { path: 'portland', component: PortlandComponent },
  { path: 'sandiego', component: SandiegoComponent },
  { path: 'tokyo', component: TokyoComponent },

];

@NgModule({
  declarations: [
    AppComponent,
    BurbankComponent,
    DavisComponent,
    SandiegoComponent,
    NewyorkComponent,
    TokyoComponent,
    PortlandComponent,
    LinksComponent
  ],
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule,
    HttpModule,
  ],
  providers: [WeatherdataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
