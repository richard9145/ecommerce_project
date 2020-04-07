# Generated by Django 3.0.3 on 2020-04-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100, verbose_name='Sub Category')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]