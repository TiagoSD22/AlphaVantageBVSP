import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BovespaStockComponent } from './bovespa-stock.component';
import {registerLocaleData} from '@angular/common';
import br from '@angular/common/locales/br';
import { ChartModule, HIGHCHARTS_MODULES } from 'angular-highcharts';
import stock from 'highcharts/modules/stock.src';
import more from 'highcharts/highcharts-more.src';
import {MatCardModule, MatSelectModule, MatButtonModule} from '@angular/material';

registerLocaleData(br, 'pt-BR');

export function highchartsModules() {
  // apply Highcharts Modules to this array
  return [stock, more];
}

@NgModule({
  imports: [
    CommonModule,
    ChartModule,
    MatCardModule,
    MatSelectModule,
    MatButtonModule
  ],
  declarations: [BovespaStockComponent],
  providers: [
    { provide: HIGHCHARTS_MODULES, useFactory: highchartsModules } // add as factory to your providers
  ]
})
export class BovespaStockModule { }
