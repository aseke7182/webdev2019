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
  public now = 0 ;
  public name: any = '';

  constructor( private  provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    });
  }
  getNewName(){
    let x = (<HTMLInputElement>document.getElementById('newName')).value;
    (<HTMLInputElement>document.getElementById('newName')).value = '';
    return x;
  }
  ChangeTask(TaskList: TaskList){
    this.now = TaskList.id;
    (<HTMLInputElement>document.getElementById('newName')).value = TaskList.name;
  }
  getTask() {
    this.provider.getTasks(this.now).then( res =>{
      this.tasks = res;
    });
  }
  deleteTaskList(){
    this.getNewName()
    this.provider.deleteTask(this.now).then(res=>{
      this.provider.getTaskLists().then(r =>{
        this.task_lists = r;
      })
    })
  }

  createTaskList(){
    this.name = this.getNewName();
    if(this.name!==''){
      this.provider.createTask(this.name).then(res =>{
        this.name = '';
        this.task_lists.push(res);
      })
    }
  }
  updateTaskList(){
    this.name = this.getNewName();
    if(this.name !== ''){
      this.provider.updateTask(this.now,this.name).then(res =>{
        this.name = '';
        this.provider.getTaskLists().then(r =>{
          this.task_lists = r;
        })
      })
    }
  }

  // createTask(){
  //   this.provider.createTaskinTask(this.tasks).then
  // }
}
