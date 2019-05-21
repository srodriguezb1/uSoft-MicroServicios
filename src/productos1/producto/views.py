from django.shortcuts import render
from .models import Producto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

# Create your views here.

def ProductosList(request):
    queryset = Producto.objects.all()
    context = list(queryset.values('id', 'nombre', 'idT', 'fechaV', 'precio', 'cantidad'))
    return JsonResponse(context, safe=False)

def MeasurementCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = Producto()
        producto.nombre = data_json['nombre']
        producto.idT = data_json['idT']
        producto.fechaV = data_json['fechaV']
        producto.precio = data_json['precio']
        producto.cantidad = data_json['cantidad']
        producto.save()
        return HttpResponse("Producto creado")
    else:
        return HttpResponse("unsuccessfully created measurement. Variable does not exist")


def pedirInfo(request):
    if request.method == 'GET':
        temp = Producto.objects.all()
        resp = ""
        for i in temp:
            resp += str(i.idT) + ";;" + str(i.nombre) + "///"
        return HttpResponse(resp)
