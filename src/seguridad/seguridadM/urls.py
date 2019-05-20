from django.conf.urls import url

from .views import (Solicitar_reporte, Solicitar_reporte_hash,KeyS,)


urlpatterns = [
    url(r'^$', Solicitar_reporte, name='SolicitarReporte'),
    url(r'^solicitarReporteHash$', Solicitar_reporte_hash, name='SolicitarReporteHash'),
    url(r'^llave$', KeyS, name='llaveS'),
]

