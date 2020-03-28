from django.urls import path
from classwork_app import views

app_name = 'classwork_app'

urlpatterns = [
    path('', views.users, name='users'),
    path('about-page/', views.about, name='about'),
    path('about-detail/<int:abt_id>', views.about_detail, name='about_detail'),
    path('post-list/<int:post_id>', views.post_list, name='post_list'),
    path('post-detail/<int:pst_id>', views.post_detail, name='post_detail'),
    path('service-page/', views.service, name='service'),
    path('service-page/<int:serve_id>', views.service_detail, name='service_detail'),
]
