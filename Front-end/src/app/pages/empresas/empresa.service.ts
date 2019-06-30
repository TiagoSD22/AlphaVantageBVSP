import { ConfigService } from './../../shared/config.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Empresa } from './empresa';
import { CompanyStock } from "./company-stock";

@Injectable({
  providedIn: 'root'
})
export class EmpresaService {

  private topCompanyUrl : string = "";
  private companyStockUrl : string = "";
  private updateCompanyUrl : string = "";

  constructor(private config : ConfigService, private http : HttpClient) {
    this.topCompanyUrl = this.config.app.urlBase.concat("/get-top-10");
    this.companyStockUrl = this.config.app.urlBase.concat("/get-company-stock");
    this.updateCompanyUrl = this.config.app.urlBase.concat("/update-company-stock");
   }

   getTopCompany(){
     return this.http.get<Array<Empresa>>(this.topCompanyUrl);
   }

   getCompanyStock(companySymbol : string){
     return this.http.get<CompanyStock>(this.companyStockUrl + "/" + companySymbol);
   }

   updateCompanyStock(companyStock : CompanyStock){
     return this.http.put(this.updateCompanyUrl, companyStock, {headers: new HttpHeaders().set('Content-Type', 'application/json')});
   }
  
}
