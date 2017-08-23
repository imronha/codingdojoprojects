import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LinksComponent } from './links/links.component';
import { ProductlistComponent } from './productlist/productlist.component';
import { CreateComponent } from './create/create.component';

const routes: Routes = [
    // { path: '', pathMatch: 'full', component: LinksComponent },
    { path: 'products', component: ProductlistComponent },
    { path: 'products/new', component: CreateComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
