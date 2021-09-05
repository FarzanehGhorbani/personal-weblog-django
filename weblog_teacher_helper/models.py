import os
import unicodedata

from django.core.files.storage import FileSystemStorage
from django.db import models
from extensions.utils import jalali_date_time_converter


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_resume_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_name = name.encode('utf-8')
    final_name = f"{new_name}{ext}"
    return f"resume/{final_name}"


class TeacherHelper(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    resume_file = models.FileField(verbose_name=' رزومه', upload_to=upload_resume_path,max_length=1000)
    created_on = models.DateTimeField(verbose_name='تاریخ ارسال رزومه',auto_now_add=True)
    is_read = models.BooleanField(verbose_name='بررسی شده / نشده', default=False)

    def jalali_publish(self):
        return jalali_date_time_converter(self.created_on)

    jalali_publish.short_description = 'تاریخ ارسال'

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست های انتخاب به عنوان کمک استاد'

