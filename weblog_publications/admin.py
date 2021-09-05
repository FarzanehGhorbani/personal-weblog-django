from django.contrib import admin

from extensions.utils import jalali_date_time_converter
from .models import Publications, Comment


# Register your models here.


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'writer', 'active_for_top','jalali_publish','count_comment']
    list_filter = ['active_for_top','year']
    list_editable = ['active_for_top']
    search_fields = ['title', 'writer','description']


admin.site.register(Publications,PublicationsAdmin)

class CommentAdmin(admin.ModelAdmin):
    def approve_comments(self, request, queryset):
        queryset.update(active=True)


    list_display = ('name', 'body', 'book', 'jalali_publish', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']




admin.site.register(Comment,CommentAdmin)