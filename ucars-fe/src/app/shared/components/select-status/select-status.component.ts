import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-select-status',
  templateUrl: './select-status.component.html',
  styleUrls: ['./select-status.component.scss']
})
export class SelectStatusComponent implements OnInit {

  @Input()
  isActive: boolean = false;

  @Input()
  readonly: boolean = false;

  statusName: string = '';

  constructor() { }

  ngOnInit(): void {
    if (this.isActive) {
      this.statusName = 'Active';
    } else {
      this.statusName = 'Inactive';
    }
  }

}
