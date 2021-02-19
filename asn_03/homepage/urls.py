from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('good.html', views.good, name = 'good.html'),
	path('ugly.html', views.ugly, name = 'ugly.html'),
]
