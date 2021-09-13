import os
import random
import string
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"Students/{final_name}"


class Students(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    rule = models.CharField(max_length=150, verbose_name='شغل')
    image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر ')
    faceBook_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس فیس بوک')
    twitter_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس توییتر')
    home_page = models.URLField(max_length=150, null=True, blank=True, verbose_name='آدرس سایت')
    description = RichTextField(verbose_name='معرفی',blank=True,null=True)
    slug = models.SlugField(blank=True, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'دانش جو'
        verbose_name_plural = 'لیست دانش جویان'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('students:info', kwargs={'slug': self.slug, 'name': self.full_name.replace(' ', '-')})
