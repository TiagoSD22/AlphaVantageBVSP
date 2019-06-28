import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CotacaoBovespaComponent } from './cotacao-bovespa.component';
import {registerLocaleData} from '@angular/common';
import br from '@angular/common/locales/br';
import { ChartModule, HIGHCHARTS_MODULES } from 'angular-highcharts';
import stock from 'highcharts/modules/stock.src';
import more from 'highcharts/highcharts-more.src';

registerLocaleData(br, 'pt-BR');

export function highchartsModules() {
  // apply Highcharts Modules to this array
  return [stock, more];
}

@NgModule({
  imports: [
    CommonModule,
    ChartModule
  ],
  declarations: [CotacaoBovespaComponent],
  providers: [
    { provide: HIGHCHARTS_MODULES, useFactory: highchartsModules } // add as factory to your providers
  ]
})
export class CotacaoBovespaModule { }
