import os
import random
import string
import unicodedata
from django.db.models import Q
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db import models
from weblog_blogs_Tags.models import Tags
from weblog_blogs_category.models import Categories
from extensions.utils import jalali_converter, jalali_date_time_converter
#from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.conf import settings

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    final_name = f"{new_name}{ext}"
    return f"blogs/{final_name}"


class BlogsManager(models.Manager):

    def get_by_Id(self, *args, **kwargs):
        blog_id = kwargs.get('id')
        qs = self.get_queryset().filter(id=blog_id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_categories(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

    def get_by_tags(self, tags_title):
        lookup = (
            Q(tags__title__icontains=tags_title)
        )
        return self.get_queryset().filter(lookup).distinct()


class Blogs(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150, verbose_name='عنوان مفاله')
    writer = models.CharField(max_length=150, verbose_name='نویسنده مقاله')
    short_description = models.CharField(max_length=150, verbose_name='توضیح کوتاه',blank=True,null=True)
    publish_date = models.DateField(verbose_name='تاریخ انتشار مقاله')
    cover = models.ImageField(verbose_name='کاور مقاله', upload_to=upload_image_path,blank=True,null=True)
    categories = models.ManyToManyField(Categories, blank=True, verbose_name=' دسته بندی ها ')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='برچسب ها')
    content=RichTextField(verbose_name='محتوی',blank=True,null=True)
    slug = models.SlugField(verbose_name='عنوان در url', blank=True, null=True)
    count_comment=models.PositiveIntegerField(verbose_name='تعدا کامنت ها',blank=True,null=True,editable=False)
    writer_image=models.ImageField(upload_to='publications/', verbose_name='تصویر نویسنده',blank=True,null=True)

    objects = BlogsManager()

    def jalali_publish(self):
        return jalali_converter(self.publish_date)

    jalali_publish.short_description = 'تاریخ ارسال'

    def get_absolute_url(self):
        return reverse('blogs:info', kwargs={'slug': self.slug, 'title': self.title.replace(' ', '-')})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title


class CommentManager(models.Manager):
    def get_active_comments(self, blog):
        return self.get_queryset().filter(blog=blog, active=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments', verbose_name='مقالات')
    name = models.CharField(max_length=80, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='نظر')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, verbose_name='فعال/غیر فعال')

    objects = CommentManager()

    def jalali_publish(self):
        return jalali_date_time_converter(self.created_on)


    jalali_publish.short_description = 'تاریخ ایجاد'

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'نظر / کامنت'
        verbose_name_plural = 'نظرات / کامنت ها'

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class ASCIIFileSystemStorage(FileSystemStorage):
    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
