from django.conf.urls import url
from .views import about, contact

urlpatterns = [
    url('about_us/', about, name="about_us"),
    url('contact_us/', contact, name="contact_us"),
]