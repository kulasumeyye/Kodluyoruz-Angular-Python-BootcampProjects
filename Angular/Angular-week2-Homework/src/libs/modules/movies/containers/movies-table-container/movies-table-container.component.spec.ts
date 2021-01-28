import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoviesTableContainerComponent } from './movies-table-container.component';

describe('MoviesTableContainerComponent', () => {
  let component: MoviesTableContainerComponent;
  let fixture: ComponentFixture<MoviesTableContainerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoviesTableContainerComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MoviesTableContainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
