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
}
