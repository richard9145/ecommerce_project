from django.urls import path
from ecommerce_app import views

app_name = 'ecommerce_app'

urlpatterns = [
    path('categories', views.categories, name='categories'),
    # path('about-page/', views.about, name='about'),
    
]