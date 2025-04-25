import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:8000/login/';

  constructor(private http: HttpClient) {}

  login(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post<any>(this.apiUrl, credentials);
  }

  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }

  register(userData: { username: string; password: string; balance: number }) {
    return this.http.post('http://localhost:8000/register/', userData);
  }  

  getProfile(): Observable<any> {
    return this.http.get('http://localhost:8000/profile/');
  }  

  logout() {
    localStorage.removeItem('access_token');
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('access_token');
  }
}
