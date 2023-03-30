from .import views
from django.contrib import admin
from django.urls import path, include
app_name='store1'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug',views.depDetail,name='depCatDetail')
]