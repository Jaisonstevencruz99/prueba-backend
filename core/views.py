from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Order, Delivery
from .serializers import ProductSerializer, OrderSerializer, DeliverySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  # 👈 IMPORTANTE
    serializer_class = ProductSerializer

    def get_queryset(self):
        tenant_id = self.request.query_params.get('tenant')
        
        if tenant_id:
            return Product.objects.filter(tenant_id=tenant_id)
        
        return Product.objects.all()

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer