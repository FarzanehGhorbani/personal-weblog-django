from django.urls import path
from .views import StudentListView,StudentsDetailView
app_name='students'
urlpatterns=[
    path('',StudentListView.as_view(),name='list'),
    path('students-<slug>/<name>/',StudentsDetailView.as_view(),name='info')
]