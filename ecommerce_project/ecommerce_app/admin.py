from django.contrib import admin
from ecommerce_app.models import Post, Category, UserProfile

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)