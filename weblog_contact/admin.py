from django.contrib import admin

# Register your models here.
from weblog_contact.models import ContactUs,ContactWay


class ContactAdmin(admin.ModelAdmin):
    def is_read_contact(self, request, queryset):
        queryset.update(is_read=True)
    is_read_contact.short_description='تایید خوانده شده ها '

    list_display = ('name', 'message', 'jalali_publish', 'is_read')
    list_filter = ('is_read', 'created_on')
    search_fields = ('name', 'email', 'message')
    list_editable = ['is_read']
    actions = ['is_read_contact']


admin.site.register(ContactUs, ContactAdmin)

admin.site.register(ContactWay)