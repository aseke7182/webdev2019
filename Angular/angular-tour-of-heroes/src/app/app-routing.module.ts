import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './components/main/main.component';
import { InfoComponent } from './components/info/info.component';
import { ProfileComponent } from './components/profile/profile.component';
import { HacknuComponent } from './components/content/hacknu/hacknu.component';
import { LoginComponent } from './components/login/login.component';
import { AccelComponent } from './components/content/accel/accel.component';

const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'info', component: InfoComponent},
  { path: 'profile', component: ProfileComponent},
  { path: 'hacknu', component: HacknuComponent},
  { path: 'login', component: LoginComponent},
  { path: 'accel', component: AccelComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
