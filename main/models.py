from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    length = models.FloatField()
    shipping_cost = models.FloatField(default=0.0) 
    status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)