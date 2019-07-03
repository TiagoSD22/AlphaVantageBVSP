import { BovespaStockModule } from './bovespa-stock.module';

describe('BovespaStockModule', () => {
  let cotacaoBovespaModule: BovespaStockModule;

  beforeEach(() => {
    cotacaoBovespaModule = new BovespaStockModule();
  });

  it('should create an instance', () => {
    expect(cotacaoBovespaModule).toBeTruthy();
  });
});
