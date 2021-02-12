import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthorizedComponent } from './layouts/authorized/authorized.component';
import { Error404Component } from './layouts/error404/error404.component';
import { UnauthorizedComponent } from './layouts/unauthorized/unauthorized.component';
import { LoginComponent } from './modules/login/login.component';
import { RegisterComponent } from './modules/register/register.component';

const routes: Routes = [
  { 
    path: '',   
    redirectTo: '/login', 
    pathMatch: 'full' 
  },
  { 
    path: '', 
    component: UnauthorizedComponent,
    children: [
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'register',
        component: RegisterComponent
      }
    ]
  },
  {
    path: 'dashboard',
    component: AuthorizedComponent
  },
  {
    path: '**',
    component: Error404Component
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
