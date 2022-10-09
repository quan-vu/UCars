import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { CarBrandRoutingModule } from './car-brand-routing.module';
import { CarBrandListPageComponent } from './pages/car-brand-list-page/car-brand-list-page.component';
import { CarBrandItemComponent } from './components/car-brand-item/car-brand-item.component';
import { CarBrandDetailPageComponent } from './pages/car-brand-detail-page/car-brand-detail-page.component';
import { AddCarBrandComponent } from './components/add-car-brand/add-car-brand.component';
import { NgbDropdownModule, NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  declarations: [
    CarBrandListPageComponent,
    CarBrandItemComponent,
    CarBrandDetailPageComponent,
    AddCarBrandComponent
  ],
  imports: [
    CommonModule,
    CarBrandRoutingModule,
    SharedModule,
    NgbModalModule,
    NgbDropdownModule,

  ]
})
export class CarBrandModule { }
