from django.db import models

class Package(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('READY', 'Ready to Pickup'),
        ('SHIPPED', 'Shipped'),
    ]

    name = models.CharField(max_length=255)
    weight = models.FloatField()
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    length = models.FloatField(default=0)
    shipping_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)