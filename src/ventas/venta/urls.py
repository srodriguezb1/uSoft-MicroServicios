
from .views import (pedirInfo, VentasList)
from django.conf.urls import url

urlpatterns = [
    url(r'^$', pedirInfo, name='pedirInfo'),
    url(r'^venta/ventasList$', VentasList, name='ventasList'),
]