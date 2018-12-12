#graphs
from django.conf.urls import url 
from .views import graph


urlpatterns = [
    url(r'^$', graph, name="graphs"),
    ]