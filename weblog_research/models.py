import os
import random
import string
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from extensions.utils import jalali_converter
from weblog_blogs.models import Blogs


class ModelManage(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class CurrentTopics(models.Model):
    title = models.CharField(verbose_name='عنوان تحقیق', max_length=200)
    content = models.CharField(verbose_name=' توضیحی کوتاه درباره تحقیق', max_length=500)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    def jalali_publish(self):
        return jalali_converter(self.created_on)

    jalali_publish.short_description='تاریخ'

    objects = ModelManage()

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'تحقیق فعلی'
        verbose_name_plural = 'لیست تحقیفات فعلی'

    def __str__(self):
        return self.title


class ResearchGrants(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان تحقیق')
    company = models.CharField(max_length=200, verbose_name='نام سازمان')
    rule = models.CharField(max_length=200, verbose_name=' نقش')
    support = models.IntegerField(verbose_name='کمک هزیته دریافتی')
    start_year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.now().year)],
        verbose_name='سال شروع',
        null=True
    )
    end_year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.now().year)],
        verbose_name='سال پایان',
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def jalali_publish(self):
        return jalali_converter(self.created_on)

    jalali_publish.short_description='تاریخ'

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'سازمان حامی'
        verbose_name_plural = 'سازمان های حامی'

    def __str__(self):
        return self.company


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"ResearchCollaborators/{final_name}"


class ResearchPartners(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    rule = models.CharField(max_length=150, verbose_name='نقش')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر ')
    faceBook_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس فیس بوک')
    twitter_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس توییتر')
    home_page = models.URLField(max_length=150, null=True, blank=True, verbose_name='آدرس سایت')
    description = RichTextField(verbose_name='معرفی',blank=True,null=True)
    blogs = models.ManyToManyField(Blogs, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    objects = ModelManage()

    def jalali_publish(self):
        return jalali_converter(self.created_on)

    jalali_publish.short_description='تاریخ'
    class Meta:
        ordering = ['-created_on']
        verbose_name = 'همکار'
        verbose_name_plural = 'لیست همکاران تحقیقاتی'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('research:researcher_info', kwargs={'slug': self.slug, 'name': self.full_name.replace(' ', '-')})