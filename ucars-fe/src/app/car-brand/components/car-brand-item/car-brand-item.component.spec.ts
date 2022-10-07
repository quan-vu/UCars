import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarBrandItemComponent } from './car-brand-item.component';

describe('CarBrandItemComponent', () => {
  let component: CarBrandItemComponent;
  let fixture: ComponentFixture<CarBrandItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarBrandItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarBrandItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
