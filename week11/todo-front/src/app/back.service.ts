import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { Task} from './task';
import { TaskList} from './task-list';
// import { HttpClient } from 'selenium-webdriver/http';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class BackService extends MainService  {

  constructor(http: HttpClient) {
    super(http);
  }
  
  getTaskList(): Promise<TaskList[]>{
    return this.get('http://127.0.0.1:8000/api/task_lists',{});
  }
  getTask(id: number): Promise<Task[]>{
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks/`,{});
  }
}
