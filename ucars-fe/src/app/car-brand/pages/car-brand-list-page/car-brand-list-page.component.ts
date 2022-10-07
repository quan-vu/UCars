import { Component, OnInit } from '@angular/core';
import { CarBrand } from 'src/core/models/car-brand.model';
import { Utils } from 'src/core/utils/utils';

@Component({
  selector: 'app-car-brand-list-page',
  templateUrl: './car-brand-list-page.component.html',
  styleUrls: ['./car-brand-list-page.component.scss']
})
export class CarBrandListPageComponent implements OnInit {

  carBrands: Array<CarBrand> = [];

  constructor() { }

  ngOnInit(): void {
    this.getMockCarBrands();
  }

  getMockCarBrands() {
    for (let i = 1; i <= 15; i++) {
      const carBrand = new CarBrand({
        id: i,
        name: `Car Brand ${i}`,
        logo: '/assets/images/no-image.png',
        description: 'Brand desctiption to long so it will be hide. Brand desctiption to long so it will be hide. Brand desctiption to long so it will be hide.',
        count_models: 1000,
        updated_at: '2022-10-25',
        is_active: Boolean(i % 2),
      });
      this.carBrands.push(carBrand);
    }
  }

}
