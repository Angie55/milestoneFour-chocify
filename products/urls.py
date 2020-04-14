from django.conf.urls import url
from .views import all_products, products_by_category, product_details

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<product_id>[-\w]+)/$', product_details, name='product_details'),
    url(r'^category/(?P<category_id>[-\w]+)/$', products_by_category,
        name='products_by_category')
]
