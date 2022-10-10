import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarBrandDetailPageComponent } from './pages/car-brand-detail-page/car-brand-detail-page.component';
import { CarBrandListPageComponent } from './pages/car-brand-list-page/car-brand-list-page.component';

const routes: Routes = [
  {
    path: '',
    component: CarBrandListPageComponent,
  },
  {
    path: 'detail/:id',
    component: CarBrandDetailPageComponent,
  },
  {
    path: 'edit/:id',
    component: CarBrandDetailPageComponent,
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CarBrandRoutingModule { }
