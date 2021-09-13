# Generated by Django 3.2.6 on 2021-09-12 07:07

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('weblog_publications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publications',
            old_name='year',
            new_name='publish_date',
        ),
        migrations.RemoveField(
            model_name='publications',
            name='description',
        ),
        migrations.AddField(
            model_name='publications',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='معرفی'),
        ),
        migrations.AddField(
            model_name='publications',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده'),
        ),
    ]
