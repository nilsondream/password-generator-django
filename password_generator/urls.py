#from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('password/', views.PasswordView, name='password'),
]
