import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { MoviesRoutingModule } from './movies-routing.module';
import { MoviesTableContainerComponent } from './containers/movies-table-container/movies-table-container.component';
import { MoviesHttpService } from './services/movies-http.service';
import { MoviesTableComponent } from './components/movies-table/movies-table.component';
import { CdkTableModule } from '@angular/cdk/table';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [MoviesTableContainerComponent, MoviesTableComponent],
  imports: [
    CommonModule,
    MoviesRoutingModule,
    HttpClientModule,
    CdkTableModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule
  ],
  providers: [
    MoviesHttpService
  ]
})
export class MoviesModule { }
