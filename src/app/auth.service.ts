import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private tokenKey = 'access_token';
  private userNameKey = 'user_name';

  constructor(private http: HttpClient, private router: Router) {}

  login(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post<any>('http://localhost:8000/api/token/', credentials).pipe(
      tap(response => {
        if (response.jwt) {
          this.saveToken(response.jwt);
          if (response.user_name) {
            localStorage.setItem(this.userNameKey, response.user_name);
          }
        }
      })
    );
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
    const token = this.getToken();
    if (!token) return false;

    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      const now = Math.floor(Date.now() / 1000);
      return payload.exp > now;
    } catch (e) {
      return false;
    }
  }

  logout() {
    localStorage.removeItem(this.tokenKey);
    localStorage.removeItem(this.userNameKey);
    this.router.navigate(['/login']);
  }

  getProfile(): Observable<any> {
    const token = localStorage.getItem('access_token');
    const headers = new HttpHeaders({
      Authorization: `Bearer ${token}`
    });

    return this.http.get('http://localhost:8000/api/profile/', { headers });
  }
}