# Generated by Django 3.2.6 on 2021-09-04 06:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='نام کتاب')),
                ('writer', models.CharField(max_length=150, verbose_name='نام نویسنده')),
                ('writer_image', models.ImageField(blank=True, null=True, upload_to='publications/', verbose_name='تصویر نویسنده')),
                ('description', models.TextField(verbose_name='معرفی')),
                ('number_of_pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='تعداد صفحات')),
                ('year', models.DateField(null=True, verbose_name='تاریخ انتشار')),
                ('image', models.ImageField(upload_to='publications/', verbose_name='تصویر کتاب')),
                ('active_for_top', models.BooleanField(default=False, help_text='فقط سه تایی که جدید هستند در صفحه انتشارات نمایش داده می شوند', verbose_name='تایید برای نمایش در بالای صفحه انتشارات و نمایش در صفحه اصلی')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('count_comment', models.PositiveIntegerField(blank=True, null=True, verbose_name='تعدا کامنت ها')),
            ],
            options={
                'verbose_name': 'کتاب',
                'verbose_name_plural': 'کتاب های منتشر شده',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='نام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('body', models.TextField(verbose_name='نظر')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='weblog_publications.publications')),
            ],
            options={
                'verbose_name': 'نظر / کامنت',
                'verbose_name_plural': 'نظرات / کامنت ها',
                'ordering': ['-created_on'],
            },
        ),
    ]
