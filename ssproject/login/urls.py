from .import views
from django.contrib import admin
from django.urls import path
app_name='login'

urlpatterns = [
      path('register',views.register,name='register'),
      path('login',views.login,name='login'),
      path('welcome',views.welcome,name='welcome'),
      path('details',views.details,name='details'),
      path('order',views.order,name='order'),



 ]
