import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BovespaStockComponent } from './bovespa-stock.component';

describe('BovespaStockComponent', () => {
  let component: BovespaStockComponent;
  let fixture: ComponentFixture<BovespaStockComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BovespaStockComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BovespaStockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
