from django.db import models

class BaseModel(models.Model):
    tenant_id = models.CharField(max_length=50)

    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.FloatField()

class Order(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Delivery(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)