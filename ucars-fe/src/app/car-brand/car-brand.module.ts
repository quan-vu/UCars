import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CarBrandRoutingModule } from './car-brand-routing.module';
import { CarBrandListPageComponent } from './pages/car-brand-list-page/car-brand-list-page.component';
import { CarBrandItemComponent } from './components/car-brand-item/car-brand-item.component';


@NgModule({
  declarations: [
    CarBrandListPageComponent,
    CarBrandItemComponent
  ],
  imports: [
    CommonModule,
    CarBrandRoutingModule
  ]
})
export class CarBrandModule { }
