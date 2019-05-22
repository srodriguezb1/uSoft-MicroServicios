from .views import (FacturasList,FacturaCreate)
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^facturas/', FacturasList, name='listaFacturas'),
    url(r'^facturasCreate/', csrf_exempt(FacturaCreate),name='facturaCreate'),
]