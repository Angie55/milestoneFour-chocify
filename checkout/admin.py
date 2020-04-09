from django.contrib import admin
from .models import Order, OrderLineItem

'''
Models registered here so they can be accessed and
edited on the admin panel
'''


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
