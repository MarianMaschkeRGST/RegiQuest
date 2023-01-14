# Generated by Django 4.1.5 on 2023-01-14 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('deadline', models.TimeField(blank=True, verbose_name='期限')),
                ('description', models.TextField(blank=True, default='', verbose_name='備考')),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL, verbose_name='メンバー')),
                ('responsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project', to=settings.AUTH_USER_MODEL, verbose_name='担当者')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
