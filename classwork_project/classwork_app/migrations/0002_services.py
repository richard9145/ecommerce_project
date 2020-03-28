# Generated by Django 3.0.3 on 2020-03-19 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classwork_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_title', models.CharField(max_length=150)),
                ('logos', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('s_content', models.TextField()),
            ],
        ),
    ]
