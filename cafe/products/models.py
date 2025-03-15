from django.db import models
from django.utils import timezone


class Product(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    infinite_stock = models.BooleanField(default=False)  

    def __str__(self):

        return self.name

class DailySale(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    amount_sold = models.IntegerField(default=0)

    class Meta:

        unique_together = ('product', 'date')

    def __str__(self):

        return f"{self.product.name} - {self.date} - Sold: {self.amount_sold}"

class ProductLog(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount_changed = models.IntegerField()
    action = models.CharField(max_length=10)  # 'add' or 'remove'
    date = models.DateField(default=timezone.now)    