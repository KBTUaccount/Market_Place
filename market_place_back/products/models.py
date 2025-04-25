from django.db import models
from users.models import CustomUser

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name