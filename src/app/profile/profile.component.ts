import {Component, OnInit} from '@angular/core';
import {RouterLink} from '@angular/router';
import {AuthService} from '../auth.service';
import {CommonModule} from '@angular/common';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [
    RouterLink,
    CommonModule,
  ],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  user: any;
  constructor(public authService: AuthService) {}

  get logged(): boolean {
    return this.authService.logged;
  }
  logout() {
    this.authService.logout();
  }
  ngOnInit() {
    this.authService.getProfile().subscribe({
      next: (data) => this.user = data,
      error: (err) => console.error('Failed to load profile', err)
    });
  }

}
