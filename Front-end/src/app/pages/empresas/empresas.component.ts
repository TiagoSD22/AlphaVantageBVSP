import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-empresas',
  templateUrl: './empresas.component.html',
  styleUrls: ['./empresas.component.scss']
})
export class EmpresasComponent implements OnInit {

  loading : boolean = true;

  constructor() { }

  ngOnInit() {
  }

  ngAfterViewInit(): void {
    this.loading = false;
  }

}
