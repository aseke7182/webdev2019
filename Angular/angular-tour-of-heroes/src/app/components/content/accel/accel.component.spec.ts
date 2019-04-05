import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AccelComponent } from './accel.component';

describe('AccelComponent', () => {
  let component: AccelComponent;
  let fixture: ComponentFixture<AccelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AccelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AccelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
