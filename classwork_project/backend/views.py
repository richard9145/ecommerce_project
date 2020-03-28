from django.shortcuts import render
from classwork_app.models import Category
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        my_content = request.POST.get('content')
        send = Category(cat_name=name, desc=my_content)
        send.save()
        messages.success(request, 'Category created successfully')
    return render(request, 'dashboard/add-category.html')
