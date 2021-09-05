# Generated by Django 3.2.6 on 2021-09-04 08:18

import django.core.validators
from django.db import migrations, models
import weblog_research.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('weblog_blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان تحقیق')),
                ('content', models.CharField(max_length=500, verbose_name=' توضیحی کوتاه درباره تحقیق')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
            ],
            options={
                'verbose_name': 'تحقیق فعلی',
                'verbose_name_plural': 'لیست تحقیفات فعلی',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ResearchGrants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان تحقیق')),
                ('company', models.CharField(max_length=200, verbose_name='نام سازمان')),
                ('rule', models.CharField(max_length=200, verbose_name=' نقش')),
                ('support', models.IntegerField(verbose_name='کمک هزیته دریافتی')),
                ('start_year', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2021)], verbose_name='سال شروع')),
                ('end_year', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2021)], verbose_name='سال پایان')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'سازمان حامی',
                'verbose_name_plural': 'سازمان های حامی',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='ResearchPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('rule', models.CharField(max_length=150, verbose_name='نقش')),
                ('image', models.ImageField(upload_to=weblog_research.models.upload_image_path, verbose_name='تصویر ')),
                ('faceBook_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='آدرس فیس بوک')),
                ('twitter_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='آدرس توییتر')),
                ('home_page', models.URLField(blank=True, max_length=150, null=True, verbose_name='آدرس سایت')),
                ('description', models.TextField(verbose_name='معرفی')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال')),
                ('blogs', models.ManyToManyField(blank=True, to='weblog_blogs.Blogs')),
            ],
            options={
                'verbose_name': 'همکار',
                'verbose_name_plural': 'لیست همکاران تحقیقاتی',
                'ordering': ['-created_on'],
            },
        ),
    ]
