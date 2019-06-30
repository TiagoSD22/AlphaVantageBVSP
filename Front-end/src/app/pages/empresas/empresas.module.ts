import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EmpresasComponent} from "./empresas.component";
import {registerLocaleData} from '@angular/common';
import br from '@angular/common/locales/br';
import { ChartModule, HIGHCHARTS_MODULES } from 'angular-highcharts';
import stock from 'highcharts/modules/stock.src';
import more from 'highcharts/highcharts-more.src';
import { NgxDatatableModule } from "@swimlane/ngx-datatable";
import {MatIconModule, MatButtonModule, MatTooltipModule} from "@angular/material";

registerLocaleData(br, 'pt-BR');

export function highchartsModules() {
  // apply Highcharts Modules to this array
  return [stock, more];
}

@NgModule({
  imports: [
    CommonModule,
    ChartModule,
    NgxDatatableModule,
    MatIconModule,
    MatButtonModule,
    MatTooltipModule
  ],
  declarations: [EmpresasComponent],
  providers: [
    { provide: HIGHCHARTS_MODULES, useFactory: highchartsModules } // add as factory to your providers
  ]
})
export class EmpresasModule { }
