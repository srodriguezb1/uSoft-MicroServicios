from django.db import models

# Create your models here.


class Caja(models.Model):
    resolucionFacturacion = models.CharField(max_length=200,null= False)
    cajaId = models.IntegerField()

    def __str__(self):
        return self.resolucionFacturacion