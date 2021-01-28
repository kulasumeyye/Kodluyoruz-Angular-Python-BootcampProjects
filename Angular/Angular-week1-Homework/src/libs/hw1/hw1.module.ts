import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { Hw1RoutingModule } from './hw1-routing.module';
import { DashboardContainerComponent } from './containers/dashboard-container/dashboard-container.component';
import { MyCardComponent } from './components/my-card/my-card.component';

import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [DashboardContainerComponent, MyCardComponent],
  imports: [
    CommonModule,
    Hw1RoutingModule,
    HttpClientModule
  ]
})
export class Hw1Module { }
