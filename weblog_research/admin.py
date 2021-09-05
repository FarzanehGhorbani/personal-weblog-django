from django.contrib import admin

from weblog_research.models import ResearchGrants, ResearchPartners, CurrentTopics


class CurrentTopicAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'content', 'active', 'jalali_publish')
    list_filter = ['active', 'created_on']
    list_editable = ['active']
    search_fields = ('name', 'email', 'body')


admin.site.register(CurrentTopics, CurrentTopicAdmin)


class ResearchGrantsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'jalali_publish']
    list_filter = ['created_on']
    search_fields = ['title', 'company', 'rule']


admin.site.register(ResearchGrants, ResearchGrantsAdmin)


class ResearchPartnersAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'rule', 'active','jalali_publish']
    list_filter = ['created_on']
    list_editable = ['active']
    search_fields = ['title', 'company', 'rule']


admin.site.register(ResearchPartners,ResearchPartnersAdmin)
