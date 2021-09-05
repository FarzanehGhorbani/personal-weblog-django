from django.urls import path
from .views import upload_file

app_name='teacher_helper'
urlpatterns = [
    path('', upload_file,name='resume')
]
