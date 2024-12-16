from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(range(0, 100))
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
