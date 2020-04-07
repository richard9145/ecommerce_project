from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    age = models.PositiveIntegerField(blank=True)
    phone= models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True) 

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name= 'Category Name')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')
    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    sub_name = models.CharField(max_length=100, verbose_name= 'Sub Category')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')
    def __str__(self):
        return self.sub_name

class Post(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads/')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    content = models.TextField()
    pst_price = models.CharField(max_length=20, verbose_name='Post Price')
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.pst_title

