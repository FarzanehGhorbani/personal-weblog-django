from django.urls import path
from .views import (StudentListAPIView,
                    StudentDetailAPIView,
                    StudentDeleteAPIView,
                    StudentUpdateAPIView,
                    StudentCreateAPIView,
                    StudentEditAPIView,
                    StudentDeleteUpdateAPIView)

app_name = 'student-api'

urlpatterns =[
    path('',StudentListAPIView.as_view(),name='student-list'),
    path('<int:id>/',StudentDetailAPIView.as_view(),name='student-detail'),
    path('<int:id>/delete',StudentDeleteAPIView.as_view(),name='student-delete'),
    path('<int:id>/update',StudentUpdateAPIView.as_view(),name='student-update'),
    path('create/',StudentCreateAPIView.as_view(),name='student-create'),
    path('<int:id>/edit',StudentEditAPIView.as_view(),name='student-edit'),
    path('<int:id>/manage/',StudentDeleteUpdateAPIView.as_view(),name='student-manage'),
]