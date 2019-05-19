from .views import pedirInfo
from django.conf.urls import url

urlpatterns = [
    url(r'^$', pedirInfo, name='pedirInfo'),
]