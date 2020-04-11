from django.db import models
import datetime
from products.models import Product


class Order(models.Model):
    '''
    Model to collect all the information we may need from the
    customer then they place an order as well as the date ordered
    and whether the order has been shipped.
    '''

    full_name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=40, blank=False)
    date_ordered = models.DateField(default=datetime.date.today, null=True)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date_ordered, self.full_name)


class OrderLineItem(models.Model):
    '''
    Model to store items the customer is purchasing in an individual
    order, the quantity of each item and the price.
    '''

    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)
