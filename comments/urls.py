from django.conf.urls import url
from .views import commentary


urlpatterns = [
    url(r'^comments/$', commentary, name="get_comments"),
]