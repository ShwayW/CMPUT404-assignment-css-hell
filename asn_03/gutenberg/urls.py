from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('1.html', views.first, name = '1.html'),
	path('2.html', views.second, name = '2.html'),
	path('3.html', views.third, name = '3.html'),
]
