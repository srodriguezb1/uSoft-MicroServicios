from django.db import models

# Create your models here.

class Venta(models.Model):
    total = models.IntegerField()
    facturaId = models.IntegerField()
    productoId = models.IntegerField()
