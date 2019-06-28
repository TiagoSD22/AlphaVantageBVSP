import { Injectable } from '@angular/core';
import { ConfigService } from './../../shared/config.service';
import { HttpClient, HttpParams } from '@angular/common/http';
import { StockQuoteData } from '../../models/stock-quote-data';

@Injectable({
  providedIn: 'root'
})
export class CotacaoBovespaService {

  private bvspIntradayUrl : string;

  constructor(private config : ConfigService, private http : HttpClient) { 
    this.bvspIntradayUrl = this.config.app.urlBase.concat("/bvsp-intraday");
  }

  calculateIntraday(timeInterval : number){
    return this.http.get<Array<StockQuoteData>>(this.bvspIntradayUrl + "/" + timeInterval.toString());
  }
}
