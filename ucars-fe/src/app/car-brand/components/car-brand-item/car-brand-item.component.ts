import { Component, Input, OnInit } from '@angular/core';
import { CarBrand } from 'src/core/models/car-brand.model';

@Component({
  selector: 'app-car-brand-item',
  templateUrl: './car-brand-item.component.html',
  styleUrls: ['./car-brand-item.component.scss']
})
export class CarBrandItemComponent implements OnInit {

  @Input()
  carBrand: CarBrand | any;

  constructor() { }

  ngOnInit(): void {
  }

}
