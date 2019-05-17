from django.shortcuts import render

# Create your views here.


from .models import Venta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def VentasList(request):
    queryset = Venta.objects.all()
    context = list(queryset.values('id', 'total'))
    return JsonResponse(context, safe=False)

def VentaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        variable = Venta()
        variable.total = data_json["total"]
        variable.save()
        return HttpResponse("successfully created variable")