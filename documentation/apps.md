---

### **App Organization**

#### **1. User Management (`users` app)**
Purpose: Manage customer and admin accounts.

- **Models**:
  - `User`
    ```python
    from django.contrib.auth.models import AbstractUser
    from django.db import models

    class User(AbstractUser):
        is_admin = models.BooleanField(default=False)
        date_joined = models.DateTimeField(auto_now_add=True)
    ```

- **Relationships**:
  - One-to-Many relationship with `Order` and `Review`.

---

#### **2. Product Management (`products` app)**
Purpose: Manage laptop product information and customer reviews.

- **Models**:
  - `Product`
    ```python
    from django.db import models

    class Product(models.Model):
        BRAND_CHOICES = [
            ('HP', 'HP'),
            ('Apple', 'Apple'),
            ('Lenovo', 'Lenovo'),
            ('Dell', 'Dell'),
        ]

        name = models.CharField(max_length=255)
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

        def __str__(self):
            return self.name
    ```

  - `Review`
    ```python
    class Review(models.Model):
        RATING_CHOICES = [(i, i) for i in range(1, 6)]

        user = models.ForeignKey('users.User', on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        rating = models.IntegerField(choices=RATING_CHOICES)
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user.username} - {self.product.name}"
    ```

- **Relationships**:
  - One-to-Many relationship:
    - `Product → Review`
    - `User → Review`

---

#### **3. Cart Management (`cart` app)**
Purpose: Handle shopping cart functionality.

- **Models**:
  - `CartItem`
    ```python
    from django.db import models

    class CartItem(models.Model):
        user = models.ForeignKey('users.User', on_delete=models.CASCADE)
        product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
        quantity = models.IntegerField()
        added_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user.username}'s cart - {self.product.name}"
    ```

- **Relationships**:
  - Many-to-One:
    - `CartItem → User`
    - `CartItem → Product`

---

#### **4. Order Management (`orders` app)**
Purpose: Manage orders and order items.

- **Models**:
  - `Order`
    ```python
    from django.db import models

    class Order(models.Model):
        STATUS_CHOICES = [
            ('Pending', 'Pending'),
            ('Confirmed', 'Confirmed'),
            ('Shipped', 'Shipped'),
            ('Delivered', 'Delivered'),
            ('Cancelled', 'Cancelled'),
        ]

        user = models.ForeignKey('users.User', on_delete=models.CASCADE)
        total_price = models.DecimalField(max_digits=10, decimal_places=2)
        status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return f"Order #{self.id} by {self.user.username}"
    ```

  - `OrderItem`
    ```python
    class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE)
        product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
        quantity = models.IntegerField()
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f"Order #{self.order.id} - {self.product.name}"
    ```

- **Relationships**:
  - One-to-Many:
    - `Order → OrderItem`
    - `User → Order`

---

#### **5. Wishlist Management (`wishlist` app)**
Purpose: Handle wishlists for users.

- **Models**:
  - `Wishlist`
    ```python
    from django.db import models

    class Wishlist(models.Model):
        user = models.ForeignKey('users.User', on_delete=models.CASCADE)
        product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
        added_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.user.username}'s wishlist - {self.product.name}"
    ```

- **Relationships**:
  - Many-to-One:
    - `Wishlist → User`
    - `Wishlist → Product`

---

### **Summary of Apps**
| **App**       | **Models**                                      | **Purpose**                              |
|---------------|-------------------------------------------------|------------------------------------------|
| `users`       | `User`                                          | Manage customer and admin accounts.      |
| `products`    | `Product`, `Review`                             | Manage products and reviews.             |
| `cart`        | `CartItem`                                      | Manage shopping cart items.              |
| `orders`      | `Order`, `OrderItem`                            | Manage orders and their items.           |
| `wishlist`    | `Wishlist`                                      | Manage user wishlists.                   |

---
