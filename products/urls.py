from django.conf.urls import url, include
from .views import all_products, products_by_category

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', products_by_category, name='products_by_category')
]
