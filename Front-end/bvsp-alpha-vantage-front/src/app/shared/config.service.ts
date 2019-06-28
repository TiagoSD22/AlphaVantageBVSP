import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ConfigService {

  private ip : string;
  public app: any;

  constructor() { 
    this.ip = window.location.origin;
    this.app = {
      name: "Template",
      urlBase: window.location.origin.substring(0,this.ip.length - 5).concat(":5000").toString()
    };
  }
}
