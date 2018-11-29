from django.conf.urls import url
from .views import get_profile


urlpatterns = [
    url(r'^profileprofile/$', get_profile, name="get_profile"),
  
]