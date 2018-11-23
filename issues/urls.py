from django.conf.urls import url, include
from .views import issues, bug


urlpatterns = [
    url(r'^$', issues, name="issues"),
    url(r'^bug/', bug, name="bug"),
    
]