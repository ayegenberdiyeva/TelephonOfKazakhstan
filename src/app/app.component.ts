import { Component, OnInit } from '@angular/core';
import { AuthService } from './auth.service';
import { RouterLink, RouterModule, Router, NavigationEnd } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FooterComponent } from './footer/footer.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    RouterLink,
    FooterComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  showFooter = true; // Control footer visibility

  constructor(public authService: AuthService, private router: Router) {}

  ngOnInit() {
    // Listen to route changes
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        // Hide footer on login and register pages
        this.showFooter = !['/login', '/register'].includes(event.urlAfterRedirects);
      }
    });
  }

  get logged(): boolean {
    return this.authService.logged;
  }

  get userName(): string | null {
    return this.authService.getUserName();
  }
}