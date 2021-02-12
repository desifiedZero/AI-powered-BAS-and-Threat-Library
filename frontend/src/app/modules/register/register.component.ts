import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  username: string = ''
  pass: string = ''
  fname: string = ''
  lname: string = ''
  c_pass: string = ''

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit() {

  }

}
