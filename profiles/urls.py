from django.conf.urls import url
from .views import get_profile, update_profile


urlpatterns = [
    url(r'^profileprofile/$', get_profile, name="get_profile"),
    url(r'^update/$', update_profile, name="update_profile"),
]