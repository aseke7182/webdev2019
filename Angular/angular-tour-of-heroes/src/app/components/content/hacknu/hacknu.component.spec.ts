import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HacknuComponent } from './hacknu.component';

describe('HacknuComponent', () => {
  let component: HacknuComponent;
  let fixture: ComponentFixture<HacknuComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HacknuComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HacknuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
