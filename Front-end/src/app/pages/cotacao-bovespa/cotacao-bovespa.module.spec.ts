import { CotacaoBovespaModule } from './cotacao-bovespa.module';

describe('CotacaoBovespaModule', () => {
  let cotacaoBovespaModule: CotacaoBovespaModule;

  beforeEach(() => {
    cotacaoBovespaModule = new CotacaoBovespaModule();
  });

  it('should create an instance', () => {
    expect(cotacaoBovespaModule).toBeTruthy();
  });
});
