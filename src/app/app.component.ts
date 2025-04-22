import { Component } from '@angular/core';
import { AuthService } from './auth.service';
import {RouterLink, RouterModule} from '@angular/router';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    RouterLink
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(public authService: AuthService) {}

  get logged(): boolean {
    return this.authService.logged;
  }
  get userName(): string | null {
    return this.authService.getUserName();
  }
}

