import { TestBed } from '@angular/core/testing';

import { BovespaStockService } from './bovespa-stock.service';

describe('BovespaStockService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BovespaStockService = TestBed.get(BovespaStockService);
    expect(service).toBeTruthy();
  });
});
