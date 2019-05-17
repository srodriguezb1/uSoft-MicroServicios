from django.shortcuts import render

# Create your views here.

from .models import Caja
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json


def CajasList(request):
    queryset = Caja.objects.all()
    context = list(queryset.values('id', 'resolucionFacturacion'))
    return JsonResponse(context, safe=False)

def CreateCaja(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        caja = Caja()
        caja.resolucionFacturacion = data_json['resolucionFacturacion']
        caja.save()
        return HttpResponse("Caja Creada")
    else:
        return HttpResponse("Caja no creada ")