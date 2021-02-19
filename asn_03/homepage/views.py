from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good(request):
	return render(request, 'homepage/good.html')


def ugly(request):
	return render(request, 'homepage/ugly.html')