from django.conf.urls import url
from .views import payment, pay, pay1


urlpatterns = [
    url(r'^payment/$', payment, name="payment"),
]