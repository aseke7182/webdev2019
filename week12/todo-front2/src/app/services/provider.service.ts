import { Injectable } from '@angular/core';
import {Task,TaskList} from '../models/models';
import {HttpClient} from '@angular/common/http';
import {MainService} from './main.service';
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists',{});
  }
  getTasks(id:number): Promise<Task[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${id}/tasks`,{});
  }
  deleteTask(id:number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}/`,{});
  }
  updateTask(id:number, newname:string): Promise<TaskList> {
    return this.put(`http://127.0.0.1:8000/api/task_lists/${id}/`,{
      name: newname
    });
  }
  createTask(newname:any): Promise<TaskList>{
    return this.post('http://127.0.0.1:8000/api/task_lists',{
      name: newname
    });
  }

  createTaskinTask(Task:Task): Promise<Task>{
    return this.post(`http://127.0.0.1:8000/api/task_lists/1/tasks`,Task)
  }

}
