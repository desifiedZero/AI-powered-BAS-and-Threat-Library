import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-authorized',
  templateUrl: './authorized.component.html',
  styleUrls: ['./authorized.component.scss']
})

export class AuthorizedComponent implements OnInit {

  title: string = 'Dashboard'

  constructor() { }

  ngOnInit(): void {
  }

}
