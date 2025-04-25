import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { AuthService } from './services/auth.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule],
  styleUrls: ['./app.component.css'],
  template: `
    <nav class="navbar">
      <div class="nav-links">
        <a routerLink="/">Home</a>
        <a routerLink="/products">Products</a>

        <ng-container *ngIf="!auth.isLoggedIn()">
          <a routerLink="/login">Login</a>
          <a routerLink="/register">Register</a>
        </ng-container>

        <ng-container *ngIf="auth.isLoggedIn()">
          <a routerLink="/profile">Profile</a>
          <button (click)="logout()">Logout</button>
        </ng-container>
      </div>
    </nav>

    <router-outlet />
  `
})
export class AppComponent {
  constructor(public auth: AuthService, private router: Router) {}

  logout() {
    this.auth.logout();
    this.router.navigate(['/login']);
  }
}
