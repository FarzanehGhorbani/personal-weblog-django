# Generated by Django 3.2.6 on 2021-09-09 17:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='معرفی'),
        ),
    ]