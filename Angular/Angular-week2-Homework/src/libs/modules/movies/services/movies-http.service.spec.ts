import { TestBed } from '@angular/core/testing';

import { MoviesHttpService } from './movies-http.service';

describe('MoviesHttpService', () => {
  let service: MoviesHttpService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MoviesHttpService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
