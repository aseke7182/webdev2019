import { Component, OnInit } from '@angular/core';
import { account } from './account';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  acc: account = {
    id: 1,
    name: 'Diana Tukenova',
    birthday: 'Nov 2, 1999',
    shortinfo: "I'm a digital designer in love with photography and painting.",
    phone: '+7 (777) 370 00 70',
    edu: 'Kazakh-British Technical University',
    email: 'd.tukenova@gmail.com'
  }
  constructor() { }

  ngOnInit() {
  }

}
