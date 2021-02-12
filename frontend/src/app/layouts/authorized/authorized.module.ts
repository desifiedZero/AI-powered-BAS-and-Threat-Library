import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthorizedComponent } from './authorized.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [
    AuthorizedComponent
  ],
  imports: [
    CommonModule,
    RouterModule
  ]
})

export class AuthorizedModule { }
