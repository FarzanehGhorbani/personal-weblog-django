from django.contrib import admin
from .models import AboutUs, Education, HonorsAndAwards


class AppAdmin(admin.ModelAdmin):

    def file_link(self, obj):
        if obj.resume:
            return "<a href='%s' download>Download</a>" % (obj.resume.url,)
        else:
            return "No attachment"

    file_link.allow_tags = True
    file_link.short_description = 'File Download'


admin.site.register(AboutUs, AppAdmin)
admin.site.register(Education)

class HonorAdmin(admin.ModelAdmin):
    list_display = ['__str__','jalali_publish']


admin.site.register(HonorsAndAwards,HonorAdmin)
