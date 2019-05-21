from .views import (CajasList)
from django.conf.urls import url

urlpatterns = [
    url(r'^$', CajasList, name='listaCaja'),
]