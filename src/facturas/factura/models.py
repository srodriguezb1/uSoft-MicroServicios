from django.db import models

# Create your models here.


class Factura(models.Model):
    tipo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    total = models.IntegerField(null=False, default=None)

    def __str__(self):
        return '%s %s' % (self.tipo, self.fecha)