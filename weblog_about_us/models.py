import os
import random
import unicodedata
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from extensions.utils import jalali_converter


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"about_me/{final_name}"

def upload_resume_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_name=name.encode('utf-8')
    final_name = f"{new_name}{ext}"
    return f"resume/{final_name}"


class AboutUs(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    Current_degree = models.CharField(max_length=150, verbose_name='بالاترین درجه فعلی')
    current_college = models.CharField(max_length=150, verbose_name='نام دانشکده فعلی')
    image = models.ImageField(verbose_name='تصویر خودتان', upload_to=upload_image_path)
    resume = models.FileField(verbose_name='رزومه', blank=True, null=True, upload_to=upload_resume_path)
    Introduction = models.TextField(verbose_name='معرفی')
    now = models.CharField(verbose_name='مدارک فعلی ', max_length=200, help_text='مستر/دکتری/پست دکتری')



    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'معرفی'
        verbose_name_plural = 'معرفی خودتان'


class Education(models.Model):
    degree = models.CharField(max_length=200, verbose_name='مدرک تحصیلی')
    university = models.CharField(max_length=200, verbose_name='دانشگاه')

    end_year = models.IntegerField(
        validators=[MaxValueValidator(datetime.now().year)],
        verbose_name='سال دریافت مدرک',
        null=True
    )

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'مدرک تحصیلی'
        verbose_name_plural = 'اطلاعات مدرک تحصیلی'


class HonorsAndAwards(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان')
    description = models.TextField(verbose_name='محتوی')
    date = models.DateField(auto_now_add=False,verbose_name='تاریخ')
    link = models.URLField(verbose_name='آدرس اینترنتی', null=True, blank=True)

    def jalali_publish(self):
        return jalali_converter(self.date)

    jalali_publish.short_description='تاریخ'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'افتخار/جایزه'
        verbose_name_plural = 'افتخارات و جوایز'


