import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CarBrandListPageComponent } from './pages/car-brand-list-page/car-brand-list-page.component';

const routes: Routes = [
  {
    path: '',
    component: CarBrandListPageComponent,
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CarBrandRoutingModule { }
