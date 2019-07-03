import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CompaniesComponent} from "./companies.component";
import {registerLocaleData} from '@angular/common';
import br from '@angular/common/locales/br';
import { NgxDatatableModule } from "@swimlane/ngx-datatable";
import {MatIconModule, MatButtonModule, MatTooltipModule} from "@angular/material";

registerLocaleData(br, 'pt-BR');

@NgModule({
  imports: [
    CommonModule,
    NgxDatatableModule,
    MatIconModule,
    MatButtonModule,
    MatTooltipModule
  ],
  declarations: [CompaniesComponent],
})
export class CompaniesModule { }
