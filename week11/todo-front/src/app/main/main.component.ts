import { Component, OnDestroy ,OnInit } from '@angular/core';
import { BackService } from '../back.service';
// import { Task } from '../task';
import {TaskList } from '../task-list';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {

  public task_lists: TaskList[] = [];
  public done = false;
  constructor(private provider: BackService) { }

  ngOnInit() {
    this.provider.getTaskList().then(res => {
      this.task_lists = res;
      this.done = true;
    });
  }

}