from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ReviewViewSet, OrderViewSet, OrderItemViewSet, UserViewSet

# Using default router to register viewsets and create URL patterns
router = DefaultRouter()

# Create a router and register the viewsets
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

# URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
