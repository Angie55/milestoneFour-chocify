from django.conf.urls import url
from .views import about, contact, privacy, terms

urlpatterns = [
    url('about_us/', about, name="about_us"),
    url('contact_us/', contact, name="contact_us"),
    url('privacy_policy/', privacy, name="privacy_policy"),
    url('terms_conditions/', terms, name="terms_conditions"),
]
