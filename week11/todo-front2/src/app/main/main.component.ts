import { Component, OnInit } from '@angular/core';
import {Task,TaskList} from '../models/models';
import {ProviderService} from '../services/provider.service';
import { now } from 'moment';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public task_lists: TaskList[] = [];
  public tasks: Task[] = [] ;
  public now = 0;

  constructor( private  provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    });
  }

  ChangeTask(TaskList: TaskList){
    this.now = TaskList.id;
  }
  getTask() {
    this.provider.getTasks(this.now).then( res =>{
      this.tasks = res;
    });
  }
}
