import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PlayermanagementComponent } from './playermanagement/playermanagement.component';
import { PlayerstatusComponent } from './playerstatus/playerstatus.component';
import { PlayerlistComponent } from './playermanagement/playerlist/playerlist.component';
import { PlayeraddComponent } from './playermanagement/playeradd/playeradd.component';
import { GamelistComponent } from './playerstatus/gamelist/gamelist.component';
import { HttpService } from "./http.service";


@NgModule({
  declarations: [
    AppComponent,
    PlayermanagementComponent,
    PlayerstatusComponent,
    PlayerlistComponent,
    PlayeraddComponent,
    GamelistComponent
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

