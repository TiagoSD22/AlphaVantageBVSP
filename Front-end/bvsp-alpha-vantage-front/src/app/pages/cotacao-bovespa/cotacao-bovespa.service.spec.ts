import { TestBed } from '@angular/core/testing';

import { CotacaoBovespaService } from './cotacao-bovespa.service';

describe('CotacaoBovespaService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CotacaoBovespaService = TestBed.get(CotacaoBovespaService);
    expect(service).toBeTruthy();
  });
});
