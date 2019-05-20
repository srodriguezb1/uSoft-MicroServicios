from django.db import models

# Create your models here.

import datetime
from cryptography.fernet import Fernet
import hmac
import hashlib
import base64

class Reporte(models.Model):
    fecha = models.DateTimeField()
    total = models.IntegerField()
    cajas = []


class HashReporte(models.Model):
    hash = models.CharField(max_length=1000)

    def calcular(Reporte, keyS):
        if Reporte is None:
            return None
        else:
            h = hmac.new(keyS, str(Reporte).encode(), hashlib.sha256)
            return h.hexdigest()

class keyS(models.Model):
    key = models.CharField(max_length=1000)

    def generar(self):
        self.key = Fernet.generate_key()