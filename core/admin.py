from django.contrib import admin


from django.contrib import admin
from .models import Tenant, Product, Order, OrderItem, Delivery

admin.site.register(Tenant)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Delivery)