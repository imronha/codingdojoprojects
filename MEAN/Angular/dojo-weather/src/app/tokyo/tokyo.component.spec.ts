import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TokyoComponent } from './tokyo.component';

describe('TokyoComponent', () => {
  let component: TokyoComponent;
  let fixture: ComponentFixture<TokyoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TokyoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TokyoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
