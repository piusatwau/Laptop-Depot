from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from api.serializers import OrderSerializer, OrderItemSerializer

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Show orders for the authenticated user, or all if the user is staff.
        """
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically assign the authenticated user as the order creator.
        """
        serializer.save(created_by=self.request.user)

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Restrict the queryset to order items of the user's orders.
        """
        if self.request.user.is_staff:
            return OrderItem.objects.all()
        return OrderItem.objects.filter(order__created_by=self.request.user)
