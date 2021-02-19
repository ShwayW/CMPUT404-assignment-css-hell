from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
	return render(request, 'gutenberg/1.html')

def second(request):
	return render(request, 'gutenberg/2.html')

def third(request):
	return render(request, 'gutenberg/3.html')