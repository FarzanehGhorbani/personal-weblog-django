from django.contrib import admin
from .models import Blogs, Comment


# Register your models here.

class Admin(admin.ModelAdmin):
    def count(self, obj):
        return obj.comments.filter(active=True).count()

    count.short_description = ' تعداد کامنت های تایید شده' 

    list_display = ['__str__', 'owner','publish_date','count','count_comment']

    class Meta:
        model = Blogs


admin.site.register(Blogs, Admin)


class CommentAdmin(admin.ModelAdmin):
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    list_display = ('name', 'body', 'blog', 'jalali_publish', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']




admin.site.register(Comment,CommentAdmin)
