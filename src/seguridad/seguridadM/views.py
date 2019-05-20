from django.shortcuts import render

# Create your views here.

from .models import Reporte
from .models import HashReporte
from .models import keyS
from cryptography.fernet import Fernet
import hmac
import hashlib
import base64

from django.http import HttpResponse


def Solicitar_reporte(request):
    # model = Reporte
    # model.traerBaseDatos(model)
    global reporte
    reporte = "Prueba"
    return HttpResponse(str(reporte))

def Solicitar_reporte_hash(request):
    global hash1
    if reporte is None:
        hash1 = None
    else:
        b = bytearray()
        b.extend(map(ord, key1))
        h = hmac.new(b, str(reporte).encode(), hashlib.sha256)
        hash1 = h.hexdigest()
    return HttpResponse(str(hash1))


def KeyS(request):
    global key1
    key1 = str('123456789')
    return HttpResponse(str(key1))