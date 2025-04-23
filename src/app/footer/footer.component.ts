import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-footer',
  //standalone: true,
  imports: [],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css'
  
})
export class FooterComponent implements OnInit{

  current_Year: number = new Date().getFullYear();
  constructor(){}

  ngOnInit(): void{

  }
}
