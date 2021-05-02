import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})

export class LoginComponent implements OnInit {

  username: string = '';
  pass: string = '';

  constructor() { }

  ngOnInit(): void {
    
  }

  onSubmit(){
    if (this.username && this.pass) {

      // all of this to be changed after creating APIs
      if (this.username == "root@localhost" && this.pass == "root"){
        alert('Hi!');
      } else {
        alert('No!');
      }
      
    }
  }

}
