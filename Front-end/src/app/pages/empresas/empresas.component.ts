import { CompanyStock } from './company-stock';
import { stock } from 'highcharts/modules/stock.src';
import { StockChart } from 'angular-highcharts';
import { Component, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { EmpresaService } from './empresa.service';
import { Empresa } from "./empresa";

@Component({
  selector: 'app-empresas',
  templateUrl: './empresas.component.html',
  styleUrls: ['./empresas.component.scss']
})
export class EmpresasComponent implements OnInit, AfterViewInit {

  loading : boolean = true;
  loadIndicator : boolean = false;
  companies : Array<Empresa> = [];
  tableSortable : boolean = true;

  constructor(private empresaService : EmpresaService,
              private toastr : ToastrService,
              private changeDetectorRefs: ChangeDetectorRef) { }

  ngOnInit() {
  }

  ngAfterViewInit(): void {
    this.loadIndicator = true
    this.empresaService.getTopCompany().subscribe(res => {
      this.companies = res["empresas"];
      this.loading = false;
      this.loadIndicator = false;
      this.toastr.clear();
      this.toastr.success("Empresas obtidas com sucesso!", "Ok", { progressBar: true, timeOut: 2000 });
    }, error => {
      this.loading = false;
      this.loadIndicator = false;
      this.toastr.clear();
      this.toastr.error("Falha ao se comunicar com o servidor!", "Ops!", { progressBar: true, timeOut: 2000 });
    });
  }

  getCompanyStock(rowIndex){
    this.loadIndicator = true;
    let symbol = this.companies[rowIndex].symbol
    this.empresaService.getCompanyStock(symbol).subscribe(res => {
      let resJson = res["stock"];
      this.companies[rowIndex].stock.price = resJson["price"];
      this.companies[rowIndex].stock.change = resJson["change"];
      this.companies[rowIndex].stock.changePercent = resJson["changePercent"];
      this.companies[rowIndex].stock.lastUpdate = resJson["lastUpdate"];
      this.companies[rowIndex].stock.volume = resJson["volume"];
      this.changeDetectorRefs.detectChanges();
      this.loadIndicator = false;
      this.toastr.clear();
      this.toastr.success("Cotação obtida", "Ok", { progressBar: true, timeOut: 2000 });
    }, error => {
      this.toastr.clear();
      this.toastr.error("Falha ao se comunicar com o servidor!", "Ops", { progressBar: true, timeOut: 2000 });
      this.loadIndicator = false;
    });
  }

  updateCompanyStock(rowIndex){
    let stock : CompanyStock = this.companies[rowIndex].stock;
    this.empresaService.updateCompanyStock(stock).subscribe(res => {
      this.toastr.clear();
      this.toastr.success("Dados atualizados em banco com sucesso!", "Ok", { progressBar: true, timeOut: 2000 });
    },error =>{
      this.toastr.clear();
      this.toastr.error("Falha ao tentar atualizar dados da empresa!", "Ops!", { progressBar: true, timeOut: 2000 });
    });
  }

  onSort(event) {
    let sortEvent = event.sorts[0];
    this.sortData(sortEvent);
  }

  sortData(sortEvent) {
    let data = this.companies
    this.companies = data.sort((a, b) => {
      const isAsc = sortEvent.dir === 'asc';
      switch (sortEvent.prop) {
        case 'rank': return this.compare(a.rank, b.rank, isAsc);
        case 'name': return this.compare(a.name, b.name, isAsc);
        case 'symbol': return this.compare(a.symbol, b.symbol, isAsc);
        case 'region': return this.compare(a.region, b.region, isAsc);
        case 'sector': return this.compare(a.sector, b.sector, isAsc);
        case 'price': return this.compare(a.stock.price, b.stock.price, isAsc);
        case 'changePercent': return this.compare(a.stock.changePercent, b.stock.changePercent, isAsc);
        case 'lastUpdate': return this.compare(a.stock.lastUpdate, b.stock.lastUpdate, isAsc);    
        default: return 0;
      }
    });
  }

  compare(a: number | string, b: number | string, isAsc: boolean) {
    return (a < b ? -1 : 1) * (isAsc ? 1 : -1);
  }

}