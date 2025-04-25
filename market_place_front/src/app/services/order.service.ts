import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = 'http://localhost:8000/orders/';

  constructor(private http: HttpClient) {}

  placeOrder(productId: number): Observable<any> {
    return this.http.post<any>(this.apiUrl + 'create/', {
      items: [
        {
          product_id: productId,
          quantity: 1
        }
      ]
    });
  }

  getMyOrders(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getOrderDetail(id: number): Observable<any> {
    return this.http.get<any>(this.apiUrl + id + '/');
  }
}
