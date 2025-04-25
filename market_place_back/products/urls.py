from django.urls import path
from products.views import ProductList, ProductDetail, category_list


app_name = "products"
urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('products/', ProductList.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
