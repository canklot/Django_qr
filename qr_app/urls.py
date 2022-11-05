from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('api_usage', views.api_usage, name='api_usage'),
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('user', views.UserView.as_view()),
    path('logout', views.LogoutView.as_view()),
]
