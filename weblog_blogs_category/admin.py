from django.contrib import admin
from .models import Categories


# Register your models here.

class Admin(admin.ModelAdmin):

    def count(self, obj):
        return obj.blogs_set.count()

    count.short_description = 'تعداد'

    list_display = ['__str__', 'name', 'count']

    class Meta:
        model = Categories


admin.site.register(Categories, Admin)
