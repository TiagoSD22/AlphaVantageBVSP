import * as Highcharts from 'highcharts';
import { Injectable } from '@angular/core';
import { StockChart } from 'angular-highcharts';

@Injectable()
export class HighchartsService {

    stock : StockChart;
    constructor() {
    }

    createChart(el, cfg) {
      
      Highcharts.chart(el, cfg);
    }
}