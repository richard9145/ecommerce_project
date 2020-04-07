from datetime import datetime
from ecommerce_app.models import Category, SubCategory


def cat_menu(request):
    category = Category.objects.all()
    kwargs = {'cat':category}
    return kwargs

def sub_menu(request):
    sub_category = SubCategory.objects.all()
    kwargs = {'sub':sub_category}
    return kwargs