from rest_framework import serializers
from products.models import Product, Review
from orders.models import Order, OrderItem
from users.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active', 'is_staff', 'date_joined']

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'description', 'image_url', 'ram', 'storage', 'processor', 'stock_quantity', 'created_at', 'updated_at', 'created_by']

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'rating', 'comment', 'created_at']

# Order Item Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'status', 'created_by', 'created_at', 'updated_at', 'items']
