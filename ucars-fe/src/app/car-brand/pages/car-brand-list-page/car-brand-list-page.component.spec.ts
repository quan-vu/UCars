import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarBrandListPageComponent } from './car-brand-list-page.component';

describe('CarBrandListPageComponent', () => {
  let component: CarBrandListPageComponent;
  let fixture: ComponentFixture<CarBrandListPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CarBrandListPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CarBrandListPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
