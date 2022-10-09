import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CarBrandFaker } from 'src/core/mock/car-brand.mock';
import { CarBrand } from 'src/core/models/car-brand.model';
import { Utils } from 'src/core/utils/utils';
import { AddCarBrandComponent } from '../../components/add-car-brand/add-car-brand.component';

@Component({
  selector: 'app-car-brand-list-page',
  templateUrl: './car-brand-list-page.component.html',
  styleUrls: ['./car-brand-list-page.component.scss']
})
export class CarBrandListPageComponent implements OnInit {

  carBrands: Array<CarBrand> = [];

  constructor(
    private modalService: NgbModal
  ) { }

  ngOnInit(): void {
    this.getCarBrands();
  }

  getCarBrands() {
    this.carBrands = CarBrandFaker.fakeCarBrands();
  }

  open() {
    const modalRef = this.modalService.open(AddCarBrandComponent, { 
      centered: true,
      size: 'lg',
    });
    modalRef.componentInstance.name = 'World';
  }

}
