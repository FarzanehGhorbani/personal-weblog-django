
from .views import footer
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('footer', footer,name='footer'),
    path('blogs/',include('weblog_blogs.urls',namespace='blogs')),
    path('contact-us/',include('weblog_contact.urls',namespace='contact')),
    path('research/',include('weblog_research.urls',namespace='research')),
    path('students/',include('weblog_students.urls',namespace='students')),
    path('publication/',include('weblog_publications.urls',namespace='publications')),
    path('teaching/',include('weblog_teaching.urls')),
    path('',include('weblog_about_us.urls',namespace='home')),
    path('teacher_helper/',include('weblog_teacher_helper.urls',namespace='teacher_helper')),
    path('blog-api/', include('weblog_blogs.api.urls',namespace='blog-api')),
    path('publication-api/', include('weblog_publications.api.urls',namespace='publication-api')),
    path('research-api/', include('weblog_research.api.urls',namespace='research-api')),
    path('student-api/', include('weblog_students.api.urls',namespace='student-api')),
    path('teaching-api/', include('weblog_teaching.api.urls',namespace='teaching-api')),
    path('content-api/', include('weblog_content.api.urls',namespace='content-api')),
    path('aboutus-api/', include('weblog_about_us.api.urls',namespace='about-us-api')),
    path('category-api/', include('weblog_blogs_category.api.urls',namespace='category-api')),
    path('tag-api/', include('weblog_blogs_Tags.api.urls',namespace='tag-api')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
