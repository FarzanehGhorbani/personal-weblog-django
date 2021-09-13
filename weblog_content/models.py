from django.db import models


# Create your models here.


class Content(models.Model):
    footer_content = models.TextField(verbose_name='متن نمایش زیرنویس سایت', blank=True, null=True)
    publication_content = models.TextField(verbose_name='متن صفحه انتشارات', blank=True, null=True)
    research_content = models.TextField(verbose_name='متن صفحه تحقیقات', blank=True, null=True)
    research_grants_content = models.TextField(verbose_name='متن صفحه انتشارات بخش کمک هزینه های تحقیقاتی', blank=True,
                                               null=True)
    research_partner_content = models.TextField(verbose_name='متن صفحه انتشارات بخش همکاران تحقیقاتی', blank=True,
                                                null=True)
    students_content = models.TextField(verbose_name='متن صفحه دانش اموزان', blank=True, null=True)
    teaching_content = models.TextField(verbose_name='متن صفحه آموزش', blank=True, null=True)
    blogs_content = models.TextField(verbose_name='متن صفحه مقالات', blank=True, null=True)
    blogs_notification_content = models.TextField(verbose_name='متن اطلاعیه صفحه مقالات', blank=True, null=True)
    contact_content = models.TextField(verbose_name='متن صفحه ارتباط', blank=True, null=True)

    class Meta:
        verbose_name = 'متن'
        verbose_name_plural = 'متن های سایت'

    def __str__(self):
        return f'متن {self.id}'
