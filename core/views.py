from rest_framework import viewsets
from .models import Product, Order, Delivery
from .serializers import *
from .mongo import db as mongo_db
from datetime import datetime

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        tenant = self.request.query_params.get("tenant_id")
        if tenant:
            return self.queryset.filter(tenant_id=tenant)
        return self.queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()

        mongo_db.events.insert_one({
            "order_id": order.id,
            "event": "CREATED",
            "timestamp": datetime.utcnow(),
            "tenant_id": order.tenant_id
        })

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer