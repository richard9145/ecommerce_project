from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ecommerce_app/index.html')

def categories(request):
    return render(request, 'ecommerce_app/categories.html')