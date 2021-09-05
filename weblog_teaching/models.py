from django.db import models


# Create your models here.

class Teaching(models.Model):
    content = models.TextField(verbose_name=' متن مبحث آموزشی')

    def __str__(self):
        if len(self.content) > 51:
            return f'{self.content[:50]}+..'
        else:
            return self.content

    class Meta:
        ordering = ['-id']
        verbose_name = 'مبحث آموزشی'
        verbose_name_plural = 'مباحث آموزشی'


class LessonList(models.Model):
    title = models.CharField(verbose_name='عنوان درس', max_length=200)
    content = models.CharField(verbose_name=' توضیحی کوتاه درباره درس', max_length=500)

    class Meta:
        ordering = ['-id']
        verbose_name = 'درس'
        verbose_name_plural = 'لیست دروس'

    def __str__(self):
        return self.title
