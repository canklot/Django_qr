from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bathroom', views.bathroom, name='bathroom'),
    path('form', views.form, name='form'),
    
]