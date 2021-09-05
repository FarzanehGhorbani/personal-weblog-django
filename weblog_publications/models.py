import random
import string
from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from extensions.utils import jalali_converter, date, jalali_date_time_converter


class Publications(models.Model):
    title = models.CharField(max_length=150, verbose_name='نام کتاب')
    writer = models.CharField(max_length=150, verbose_name='نام نویسنده')
    writer_image=models.ImageField(upload_to='publications/', verbose_name='تصویر نویسنده',blank=True,null=True)
    description = models.TextField(verbose_name='معرفی')
    number_of_pages = models.IntegerField(
        validators=[
            MinValueValidator(1)],
        verbose_name='تعداد صفحات'
    )
    year = models.DateField(verbose_name='تاریخ انتشار', null=True)
    image = models.ImageField(upload_to='publications/', verbose_name='تصویر کتاب')
    active_for_top = models.BooleanField(help_text='فقط سه تایی که جدید هستند در صفحه انتشارات نمایش داده می شوند',verbose_name='تایید برای نمایش در بالای صفحه انتشارات و نمایش در صفحه اصلی', default=False)
    slug = models.SlugField(blank=True, unique=True,null=True)
    count_comment = models.PositiveIntegerField(verbose_name='تعدا کامنت ها', blank=True, null=True)
    def jalali_publish(self):
        return jalali_converter(self.year)

    jalali_publish.short_description = 'تاریخ انتشار'

    def get_persian_year(self):
        return date(self.year)

    class Meta:
        ordering = ['-id']
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب های منتشر شده'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('publications:info', kwargs={'slug': self.slug, 'name': self.title.replace(' ', '-')})

class CommentManager(models.Manager):
    def get_active_comments(self, book):
        return self.get_queryset().filter(book=book, active=True)


class Comment(models.Model):
    book = models.ForeignKey(Publications,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80,verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='نظر')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    objects = CommentManager()

    def jalali_publish(self):
        return jalali_date_time_converter(self.created_on)
    jalali_publish.short_description='تاریخ ایجاد'

    class Meta:
        ordering = ['-created_on']
        verbose_name='نظر / کامنت'
        verbose_name_plural='نظرات / کامنت ها'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

