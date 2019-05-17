from django.db import models

# Create your models here.


class Caja(models.Model):
    resolucionFacturacion = models.CharField(max_length=200,null= False)

    def __str__(self):
        return self.resolucionFacturacion