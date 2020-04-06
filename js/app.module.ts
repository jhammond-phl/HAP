import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {Pipe, PipeTransform} from '@angular/core';

@NgModule({
  imports:      [ BrowserModule ],
  providers:    [ Logger ],
  declarations: [ AppComponent ],
  exports:      [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }


