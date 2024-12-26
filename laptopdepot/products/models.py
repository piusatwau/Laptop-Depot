from django.db import models
from users.models import User


# Products Model
class Product(models.Model):
    # Laptop Options
    HP = 'HP'
    APPLE = 'Apple'
    LENOVO = 'Lenovo'
    DELL = 'Dell'

    BRAND_CHOICES = [
        (HP, 'HP'),
        (APPLE, 'Apple'),
        (LENOVO, 'Lenovo'),
        (DELL, 'Dell'),
    ]

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField()
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


# Reviews Model
class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
