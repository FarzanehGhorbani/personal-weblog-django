from django.contrib import admin

# Register your models here.
from weblog_students.models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('__str__','active', 'created_on')
    list_filter = ['active', 'created_on']
    list_editable = ['active']
    search_fields = ('__str__', 'rule', 'description')


admin.site.register(Students, StudentsAdmin)