from django.db import models


class ProductType(models.Model):
    code_id = models.CharField(max_length=15)
    name = models.CharField(max_length=31)
    descn = models.TextField()

    class Meta:
        ordering = ['name']


class Product(models.Model):
    uid = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType,
                                     on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        ordering = ['name']
