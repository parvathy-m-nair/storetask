from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import render
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)








    class meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('store1:products_by_category',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=250, unique=True)
    coursefee = models.DecimalField(max_digits=250, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('store1:depCatDetail',args=[self.category.slug,self.slug])
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'



    def __str__(self):
        return '{}'.format(self.name)





