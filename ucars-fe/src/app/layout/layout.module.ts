import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
// import { FlexLayoutModule } from "@angular/flex-layout";
import { MainLayoutComponent } from './main-layout/main-layout.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { LayoutRoutingModule } from './layout-routing.module';
// import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  imports: [
    CommonModule,
    LayoutRoutingModule,
    // NgbModule,
    // FlexLayoutModule,
  ],
  exports: [],
  declarations: [
    MainLayoutComponent,
    FooterComponent,
    HeaderComponent,
    SidebarComponent
  ]
})
export class LayoutModule { }
