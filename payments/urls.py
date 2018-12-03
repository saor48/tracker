from django.conf.urls import url
from .views import payment, pay, pay1


urlpatterns = [
    url(r'^pay/$', pay, name="pay"),
    url(r'^pay1/$', pay1, name="pay1"),
    url(r'^payment/$', payment, name="payment"),
]