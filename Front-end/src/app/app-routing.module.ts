import { NgModule } from '@angular/core';
import { Route, RouterModule } from '@angular/router';
import { CotacaoBovespaComponent } from "./pages/cotacao-bovespa/cotacao-bovespa.component";
import { EmpresasComponent } from "./pages/empresas/empresas.component";

const routes: Route[] = [
  {path : "cotacao-bovespa", component : CotacaoBovespaComponent},
  {path : "empresas", component : EmpresasComponent},
  {path : "", redirectTo : "cotacao-bovespa", pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
