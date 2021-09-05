import random
import string
import unicodedata
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse


class Tags(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان', help_text='عنوان با منحصر به فردباشد')
    slug=models.SlugField(blank=True,null=True,verbose_name='عنوان در url',unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال ')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogs:search', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تگ/برچسب'
        verbose_name_plural = 'تگ ها / برچست ها'


class ASCIIFileSystemStorage(FileSystemStorage):
    def get_valid_name(self, name):
        title = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        return super(ASCIIFileSystemStorage, self).get_valid_name(title)