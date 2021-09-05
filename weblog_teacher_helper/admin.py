from django.contrib import admin
from .models import TeacherHelper


class Admin(admin.ModelAdmin):
    list_display = ['__str__', 'jalali_publish', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read', 'created_on']


admin.site.register(TeacherHelper, Admin)
