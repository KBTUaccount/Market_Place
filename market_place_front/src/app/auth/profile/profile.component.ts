import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  username: string = '';
  balance: number = 0;
  products: any[] = [];
  orders: any[] = [];
  loading: boolean = true;
  error: string = '';

  constructor(private auth: AuthService) {}

  ngOnInit(): void {
    this.auth.getProfile().subscribe({
      next: (data) => {
        this.username = data.username;
        this.balance = data.balance;
        this.products = data.products || [];
        this.orders = data.orders || [];
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load profile.';
        this.loading = false;
        console.error(err);
      }
    });
  }
}
