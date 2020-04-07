from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images', default='')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.id])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, null=True)
    title = models.CharField(max_length=150, default='')
    introduction = models.TextField(max_length=400)
    details = models.TextField(default='')
    ingredients = models.TextField(default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    milk_choc = models.BooleanField(default=True)
    white_choc = models.BooleanField(default=False)
    dark_choc = models.BooleanField(default=False)
    tags = models.CharField(max_length=300)
    image1 = models.ImageField(upload_to='images', blank=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    image4 = models.ImageField(upload_to='images', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('product_details', args=[self.id])

    def __str__(self):
        return self.title
