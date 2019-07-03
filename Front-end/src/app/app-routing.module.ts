import { NgModule } from '@angular/core';
import { Route, RouterModule } from '@angular/router';
import { BovespaStockComponent } from "./pages/bovespa-stock/bovespa-stock.component";
import { CompaniesComponent } from "./pages/companies/companies.component";

const routes: Route[] = [
  {path : "cotacao-bovespa", component : BovespaStockComponent},
  {path : "empresas", component : CompaniesComponent},
  {path : "", redirectTo : "cotacao-bovespa", pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
