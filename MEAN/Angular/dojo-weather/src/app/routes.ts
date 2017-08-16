import { BurbankComponent } from './burbank/burbank.component';
import { DavisComponent } from './davis/davis.component';
import { NewyorkComponent } from './newyork/newyork.component';
import { PortlandComponent } from './portland/portland.component';
import { SandiegoComponent } from './sandiego/sandiego.component';
import { TokyoComponent } from './tokyo/tokyo.component';
import { LinksComponent } from './links/links.component';
import { Routes, RouterModule } from '@angular/router';

const APP_ROUTES: Routes = [
    // { path: '', component: LinksComponent , pathMatch: 'full' },
    { path: 'burbank', component: BurbankComponent },
    { path: 'davis', component: DavisComponent },
    { path: 'newyork', component: NewyorkComponent },
    { path: 'sandiego', component: SandiegoComponent },
    { path: 'tokyo', component: TokyoComponent },
    { path: 'portland', component: PortlandComponent }
];
export const routing = RouterModule.forRoot(APP_ROUTES);
