from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views her
from django.db.models.expressions import result
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Category, Product


# Create your views here.
def allProdCat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug != None:
        c_slug = get_object_or_404(Category, slug=c_slug)
        products = Product.objects.all().filter(category=c_page)

        return HttpResponseRedirect("http://google.com/")
    else:
        products = Product.objects.all().filter


    return render(request, 'category.html', {'category': c_page, 'products': products})


def depDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'product.html', {'product': product})



























