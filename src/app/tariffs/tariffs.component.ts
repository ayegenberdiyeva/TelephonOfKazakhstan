import { Component, OnInit } from '@angular/core';
import { TariffsService } from '../tariffs.service';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-tariffs',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './tariffs.component.html',
  styleUrls: ['./tariffs.component.css'],
})
export class TariffsComponent implements OnInit {
  tariffs: any[] = [];

  constructor(private tariffsService: TariffsService) {}

  ngOnInit() {
    this.tariffsService.getTariffs().subscribe((data) => {
      this.tariffs = data;
    });
  }
}
