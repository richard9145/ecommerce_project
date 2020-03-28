from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-category/', views.add_category, name='add_category'),
]
