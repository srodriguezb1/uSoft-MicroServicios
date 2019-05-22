
from .views import (pedirInfo, VentasList, VentaCreate)
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', pedirInfo, name='pedirInfo'),
    url(r'^ventasList/', VentasList, name='ventasList'),
    url(r'^createVenta/', csrf_exempt(VentaCreate), name='ventaCreate')
]