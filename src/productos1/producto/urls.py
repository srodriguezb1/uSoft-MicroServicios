from .views import (pedirInfo,ProductosList,ProductosCreate)
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', pedirInfo, name='pedirInfo'),
    url(r'^productosList/', ProductosList, name='productosList'),
    url(r'^productosCreate/$', csrf_exempt(ProductosCreate), name='productoCreate'),
]