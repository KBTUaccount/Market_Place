import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProductService } from '../../services/product.service';
import { CategoryService } from '../../services/category.service';
import { OrderService } from '../../services/order.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-products-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products-list.component.html',
  styleUrls: ['./products-list.component.css']
})
export class ProductsListComponent implements OnInit {
  products: any[] = [];
  categories: any[] = [];
  selectedCategory: number = 0;

  constructor(
    private productService: ProductService,
    private categoryService: CategoryService,
    private orderService: OrderService,
    public auth: AuthService
  ) {}

  ngOnInit(): void {
    this.loadProducts();
    this.loadCategories();
  }

  loadProducts() {
    this.productService.getProducts().subscribe({
      next: (data) => {
        this.products = data;
      },
      error: (err) => {
        console.error('Error loading products:', err);
      }
    });
  }

  loadCategories() {
    this.categoryService.getCategories().subscribe({
      next: (data) => {
        this.categories = data;
      },
      error: (err) => {
        console.error('Error loading categories:', err);
      }
    });
  }

  buyProduct(productId: number) {
    this.orderService.placeOrder(productId).subscribe({
      next: () => {
        alert(`✅ You successfully bought product #${productId}`);
      },
      error: (err) => {
        console.error('Error buying product:', err);
        alert(`❌ Could not complete purchase`);
      }
    });
  }

  filteredProducts() {
    if (this.selectedCategory === 0) {
      return this.products;
    }
    return this.products.filter(product => product.category === this.selectedCategory);
  }
}
