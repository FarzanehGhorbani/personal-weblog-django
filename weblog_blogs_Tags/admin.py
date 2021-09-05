from django.contrib import admin
from .models import Tags
# Register your models here.

class Admin(admin.ModelAdmin):

    def count(self, obj):
        return obj.blogs_set.count()

    count.short_description = 'تعداد'

    list_display = ['__str__', 'title', 'count','active']
    list_editable = ['active']

    class Meta:
        model = Tags

admin.site.register(Tags,Admin)