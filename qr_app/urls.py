from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('api_usage', views.api_usage, name='api_usage'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    
]
