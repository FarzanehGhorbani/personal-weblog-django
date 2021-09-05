from django.db import models


# Create your models here.
from extensions.utils import jalali_date_time_converter


class ContactUs(models.Model):
    name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل')
    subject = models.CharField(max_length=150, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیغام')
    created_on = models.DateTimeField(verbose_name='تاریخ', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='خوانده شده / نشده', default=False)

    def jalali_publish(self):
        return jalali_date_time_converter(self.created_on)

    jalali_publish.short_description = 'تاریخ دریافت پیام'

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.subject


class ContactWay(models.Model):
    college_address = models.TextField(verbose_name='آدرس دانشگاه', null=True, blank=True)
    office_address = models.TextField(verbose_name='آدرس دفتر', null=True, blank=True)
    office_phone = models.CharField(max_length=20, verbose_name='شماره تلفن دفتر', null=True, blank=True)
    internal_phone = models.CharField(max_length=20, verbose_name='شماره تلفن داخلی دفتر', null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name='شماره همراه', null=True, blank=True)
    fax = models.CharField(max_length=20, verbose_name='فکس', null=True, blank=True)
    faceBook_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس فیس بوک')
    twitter_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس توییتر')
    googlePlus_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس گوگل پلاس')
    linkedin_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس لینکدین')
    skype_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس اسکایپ')
    instagram_url = models.CharField(max_length=150, null=True, blank=True, verbose_name='آدرس اینستاگرام')

    class Meta:
        verbose_name = 'راه ارتباطی'
        verbose_name_plural = 'راه های ارتباطی کاربران'

    def __str__(self):
        return self.college_address