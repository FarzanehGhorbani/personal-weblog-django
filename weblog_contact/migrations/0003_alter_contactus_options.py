# Generated by Django 3.2.6 on 2021-08-28 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog_contact', '0002_auto_20210828_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'ordering': ['-created_on'], 'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
    ]