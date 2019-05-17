from django.shortcuts import render

# Create your views here.


from .models import Factura
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def FacturasList(request):
    queryset = Factura.objects.all()
    context = list(queryset.values('id', 'tipo', 'fecha', 'total'))
    return JsonResponse(context, safe=False)

def FacturaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        factura = Factura()
        factura.tipo = data_json['tipo']
        factura.fecha = data_json['fecha']
        factura.total = data_json['total']
        factura.save()
        return HttpResponse("Factura creada")
    else:
        return HttpResponse("unsuccessfully created measurement. Variable does not exist")