import unicodedata

from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در url ',unique=True)

    def get_absolute_url(self):
        return reverse('blogs:categories', kwargs={'category_name': self.name})


    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'

    def __str__(self):
        return self.title

class ASCIIFileSystemStorage(FileSystemStorage):
    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
