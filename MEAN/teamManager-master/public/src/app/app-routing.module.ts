import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PlayermanagementComponent } from './playermanagement/playermanagement.component';
import { PlayerstatusComponent } from './playerstatus/playerstatus.component';
import { PlayerlistComponent } from './playermanagement/playerlist/playerlist.component';
import { PlayeraddComponent } from './playermanagement/playeradd/playeradd.component';
import { GamelistComponent } from './playerstatus/gamelist/gamelist.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: "full",
    redirectTo:"/players/list"
  },
  {
    path: "players",    
    component: PlayermanagementComponent,
    children: [
      {path:"add", component:PlayeraddComponent},
      {path:"list", component:PlayerlistComponent}
      ]
  },
  {
    path: "status",
    component: PlayerstatusComponent,
    children:[
      {path:"game/:game", component:GamelistComponent},
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
