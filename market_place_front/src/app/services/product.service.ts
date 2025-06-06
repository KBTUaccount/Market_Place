import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://localhost:8000/products/';

  constructor(private http: HttpClient) {}

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
  
  createProduct(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
  
  deleteProduct(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}${id}/`);
  }
  
}
