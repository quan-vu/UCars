import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SelectStatusComponent } from './components/select-status/select-status.component';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';



@NgModule({
  declarations: [
    SelectStatusComponent
  ],
  imports: [
    CommonModule,
    NgbDropdownModule,
  ],
  exports: [
    SelectStatusComponent,
  ]
})
export class SharedModule { }
