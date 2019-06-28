import { NgModule } from '@angular/core';
import { Route, RouterModule } from '@angular/router';
import { CotacaoBovespaComponent } from "./pages/cotacao-bovespa/cotacao-bovespa.component";

const routes: Route[] = [
  {path : "cotacao-bovespa", component : CotacaoBovespaComponent},
  {path : "", component : CotacaoBovespaComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
