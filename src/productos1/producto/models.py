from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length = 100, blank = True,null=True)
    idT = models.IntegerField(null=False, default=None)
    fechaV = models.DateTimeField(auto_now_add=True, auto_now=False)
    precio = models.FloatField(null=True, blank=True, default=None)
    cantidad = models.IntegerField(null=False, default=None)

    def __unicode__(self):
        return self.idT

    def __str__(self):
        return self.nombre