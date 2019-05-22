from .views import (CajasList, CreateCaja)
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^cajas/', CajasList, name='listaCaja'),
    url(r'^cajasCreate/', csrf_exempt(CreateCaja), name='crearCaja')
]


