import { LinksComponent } from './links/links.component';
import { MainComponent } from './main/main.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductCreationComponent } from './product-creation/product-creation.component';
import { Routes, RouterModule } from '@angular/router';

const APP_ROUTES: Routes = [
    // { path: '', component: LinksComponent , pathMatch: 'full' },
    { path: 'products', component: ProductListComponent },
];
export const routing = RouterModule.forRoot(APP_ROUTES);
