import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarBrandDetailPageComponent } from './car-brand-detail-page.component';

describe('CarBrandDetailPageComponent', () => {
  let component: CarBrandDetailPageComponent;
  let fixture: ComponentFixture<CarBrandDetailPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarBrandDetailPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarBrandDetailPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
