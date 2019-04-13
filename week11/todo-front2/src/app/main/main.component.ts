import { Component, OnInit } from '@angular/core';
import {Task,TaskList} from '../models/models';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public task_lists: TaskList[] = [];
  public tasks: Task[] = [] ;

  constructor( private  provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    });
  }
  getTask(taskList: TaskList) {
    this.provider.getTasks(taskList.id).then( res =>{
      this.tasks = res;
    });
  }
}
