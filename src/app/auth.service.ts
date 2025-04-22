import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private tokenKey = 'access_token';
  private userNameKey = 'user_name';

  constructor(private http: HttpClient, private router: Router) {}

  login(credentials: { username: string; password: string }) {
    return this.http.post<any>('http://localhost:8000/api/token/', credentials);
  }


  saveToken(token: string) {
    localStorage.setItem(this.tokenKey, token);
  }
  getUserName(): string | null {
    return localStorage.getItem(this.userNameKey);
  }

  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  get logged(): boolean {
    return !!this.getToken();
  }

  logout() {
    localStorage.removeItem(this.tokenKey);
    this.router.navigate(['/login']);
  }

  getProfile() {
    return this.http.get<{ name: string, surname: string, username: string, tariff: any }>('http://localhost:8000/api/profile/');
  }


}
