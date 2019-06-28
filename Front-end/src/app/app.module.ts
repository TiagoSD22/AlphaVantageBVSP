import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { HighchartsService } from './shared/services/highcharts.service';
import {ToastrModule} from 'ngx-toastr';
import { EmpresasModule } from './pages/empresas/empresas.module';
import { CotacaoBovespaModule } from './pages/cotacao-bovespa/cotacao-bovespa.module';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    CotacaoBovespaModule,
    EmpresasModule,
    ToastrModule.forRoot()
  ],
  providers: [HighchartsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
