import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LinksComponent } from './links/links.component';
import { ProductlistComponent } from './productlist/productlist.component';
import { CreateComponent } from './create/create.component';
import { FormsModule } from '@angular/forms'
@NgModule({
  declarations: [
    AppComponent,
    LinksComponent,
    ProductlistComponent,
    CreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
