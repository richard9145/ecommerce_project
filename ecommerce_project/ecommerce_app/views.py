from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_app.models import Category, Post, SubCategory

# Create your views here.

def index(request):
    return render(request, 'ecommerce_app/index.html')

def categories(request):
    return render(request, 'ecommerce_app/categories.html')