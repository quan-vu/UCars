import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CarBrandRoutingModule } from './car-brand-routing.module';
import { CarBrandListPageComponent } from './pages/car-brand-list-page/car-brand-list-page.component';
import { CarBrandItemComponent } from './components/car-brand-item/car-brand-item.component';
import { CarBrandDetailPageComponent } from './pages/car-brand-detail-page/car-brand-detail-page.component';


@NgModule({
  declarations: [
    CarBrandListPageComponent,
    CarBrandItemComponent,
    CarBrandDetailPageComponent
  ],
  imports: [
    CommonModule,
    CarBrandRoutingModule
  ]
})
export class CarBrandModule { }
