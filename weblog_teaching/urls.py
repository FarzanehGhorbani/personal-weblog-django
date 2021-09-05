from django.urls import path
from .views import teaching_page

urlpatterns=[
    path('',teaching_page,name='teaching')
]