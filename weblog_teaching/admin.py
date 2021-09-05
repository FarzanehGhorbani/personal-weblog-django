from django.contrib import admin

from weblog_teaching.models import LessonList, Teaching


class Admin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['__str__', 'content']


admin.site.register(LessonList,Admin)
admin.site.register(Teaching)
