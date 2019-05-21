from .views import (FacturasList)
from django.conf.urls import url

urlpatterns = [
    url(r'^$', FacturasList, name='listaFacturas'),
]