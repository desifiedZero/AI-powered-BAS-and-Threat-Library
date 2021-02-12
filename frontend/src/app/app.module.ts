import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UnauthorizedComponent } from './layouts/unauthorized/unauthorized.component';
import { AuthorizedComponent } from './layouts/authorized/authorized.component';
import { RouterModule } from '@angular/router';
import { UnauthorizedModule } from './layouts/unauthorized/unauthorized.module';
import { AuthorizedModule } from './layouts/authorized/authorized.module';
import { FormsModule } from '@angular/forms';
import { Error404Component } from './layouts/error404/error404.component';

@NgModule({
  declarations: [
    AppComponent,
    Error404Component,
  ],
  imports: [
    BrowserModule,
    RouterModule, 
    AppRoutingModule,
    UnauthorizedModule,
    AuthorizedModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
