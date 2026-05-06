from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import *

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'deliveries', DeliveryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]