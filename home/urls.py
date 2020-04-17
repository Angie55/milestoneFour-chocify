from django.conf.urls import url
from .views import about

urlpatterns = [
    url('about_us/', about, name="about_us"),
]
