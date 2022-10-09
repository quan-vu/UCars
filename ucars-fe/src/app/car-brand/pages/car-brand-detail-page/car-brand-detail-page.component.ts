import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CarBrand } from 'src/core/models/car-brand.model';

@Component({
  selector: 'app-car-brand-detail-page',
  templateUrl: './car-brand-detail-page.component.html',
  styleUrls: ['./car-brand-detail-page.component.scss']
})
export class CarBrandDetailPageComponent implements OnInit {

  carBrand: CarBrand = {
    id: 1,
    name: 'Fake Car Brand',
    logo: '/assets/images/no-image.png',
    description: 'This is a fake car brand',
    count_models: 1000,
    updated_at: '2022-10-01',
    is_active: true,
    map: function (obj: any): void {
      throw new Error('Function not implemented.');
    }
  }

  isEditMode: boolean = false;

  constructor(
    private route: ActivatedRoute,
  ) { 
    const id = this.route.snapshot.paramMap.get('id') || null;
    this.isEditMode = this.route.snapshot.routeConfig && this.route.snapshot.routeConfig?.path?.includes('edit') ? true : false;
    console.log("isEditMode: ", this.isEditMode);
  }

  ngOnInit(): void {
  }

}
