import { Component, OnInit } from '@angular/core';
import {NgbActiveModal, NgbModal} from '@ng-bootstrap/ng-bootstrap';
import { CarBrand } from 'src/core/models/car-brand.model';

@Component({
  selector: 'app-add-car-brand',
  templateUrl: './add-car-brand.component.html',
  styleUrls: ['./add-car-brand.component.scss']
})
export class AddCarBrandComponent implements OnInit {

  carBrand: CarBrand = {
    id: 0,
    name: '',
    logo: '',
    description: '',
    count_models: 0,
    updated_at: '',
    is_active: true,
    map: function (obj: any): void {
      throw new Error('Function not implemented.');
    }
  }
  
  constructor(public activeModal: NgbActiveModal) {}

  ngOnInit(): void {
  }

}
