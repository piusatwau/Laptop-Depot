# Laptop Depot API Design and Implementation Blueprint

#### API Endpoints Documentation

| Endpoint         | Method | Description                              | Request Parameters                        | Example Response                        |
|------------------|--------|------------------------------------------|------------------------------------------|-----------------------------------------|
| `/products/`     | GET    | Retrieve a list of all laptops.          | `brand` (optional), `price_range` (optional) | JSON list of products.                  |
| `/products/<id>` | GET    | Retrieve details of a specific laptop.   | `id` (required)                           | JSON object with laptop details.        |
| `/cart/`         | POST   | Add a laptop to the user's cart.         | `product_id`, `quantity`                  | Success message with updated cart info. |
| `/cart/`         | GET    | Retrieve the current user's cart items.  | None                                      | JSON list of cart items.                |
| `/cart/<id>`     | DELETE | Remove a laptop from the user's cart.    | `id` (required)                           | Success message with updated cart info. |
| `/users/login/`  | POST   | User authentication and token retrieval. | `username`, `password`                    | JSON object with token.                 |
| `/users/signup/` | POST   | Create a new user account.               | `username`, `email`, `password`           | JSON object with user info.             |

#### Example Request/Response

**GET `/products/`**
```http
GET /products/
```
Request:
```
{
    "brand": "Dell",
    "price_range": "1000-2000"
}
```
Response:
```json
[
    {
        "id": 1,
        "brand": "Dell",
        "model": "Inspiron 15",
        "price": 1500,
        "specs": {
            "RAM": "16GB",
            "Storage": "512GB SSD"
        }
    },
    ...
]
```

---

### 1. Proof of Concept

#### Steps
1. Implementation of the `/products/` and `/users/login/` endpoints in the Django project.
2. Test the endpoints using Postman or curl.
3. Authentication using Django Rest Framework's (DRF) token-based authentication.

#### Example Implementation

**Code for `/products/` Endpoint:**
```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def product_list(request):
    brand = request.GET.get('brand')
    price_range = request.GET.get('price_range')

    products = Product.objects.all()

    if brand:
        products = products.filter(brand__iexact=brand)

    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
        products = products.filter(price__gte=min_price, price__lte=max_price)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
```

**Postman Test Example:**
- Request: `GET /products/?brand=Dell`
- Response:
```json
[
    {
        "id": 1,
        "brand": "Dell",
        "model": "Inspiron 15",
        "price": 1500,
        "specs": {
            "RAM": "16GB",
            "Storage": "512GB SSD"
        }
    }
]
```


---

### 2. Add Authentication
#### Deliverable
- Implement authentication for the API using DRF's token-based authentication.

#### Implementation
1. Install DRF token authentication:
   ```bash
   pip install djangorestframework djangorestframework-simplejwt
   ```
2. Update `settings.py`:
   ```python
   INSTALLED_APPS += [
       'rest_framework',
       'rest_framework_simplejwt',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': (
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ),
   }
   ```
3. Create login and token retrieval endpoints:
   ```python
   from rest_framework_simplejwt.views import TokenObtainPairView

   urlpatterns = [
       path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   ]
   ```
4. Protect other endpoints using `@permission_classes([IsAuthenticated])`.

#### Testing Authentication
- Test token generation using Postman or curl:
```http
POST /users/login/
{
    "username": "testuser",
    "password": "password123"
}
```
Response:
```json
{
    "access": "<JWT_TOKEN>",
    "refresh": "<JWT_REFRESH_TOKEN>"
}
```

