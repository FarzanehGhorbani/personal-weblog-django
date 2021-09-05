"""personal_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from .views import footer,header
from django.contrib import admin
from django.urls import path, include

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
    path('teacher_helper/',include('weblog_teacher_helper.urls',namespace='teacher_helper'))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)