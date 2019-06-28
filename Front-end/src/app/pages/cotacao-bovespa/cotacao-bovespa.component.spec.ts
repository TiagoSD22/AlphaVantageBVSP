import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CotacaoBovespaComponent } from './cotacao-bovespa.component';

describe('CotacaoBovespaComponent', () => {
  let component: CotacaoBovespaComponent;
  let fixture: ComponentFixture<CotacaoBovespaComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CotacaoBovespaComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CotacaoBovespaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
