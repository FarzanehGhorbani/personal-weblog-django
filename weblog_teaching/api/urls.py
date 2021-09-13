from django.urls import path
from .views import (TeachingListAPIView,
                    TeachingDetailAPIView,
                    TeachingDeleteAPIView,
                    TeachingUpdateAPIView,
                    TeachingCreateAPIView,
                    TeachingEditAPIView,
                    TeachingDeleteUpdateAPIView,
                    
                    LessonListAPIView,
                    LessonListDetailAPIView,
                    LessonListDeleteAPIView,
                    LessonListUpdateAPIView,
                    LessonListCreateAPIView,
                    LessonListEditAPIView,
                    LessonListDeleteUpdateAPIView)
app_name = 'teaching-api'

urlpatterns =[
    path('teaching/',TeachingListAPIView.as_view(),name='teaching-list'),
    path('teaching/<int:id>/',TeachingDetailAPIView.as_view(),name='teaching-detail'),
    path('teaching/<int:id>/delete',TeachingDeleteAPIView.as_view(),name='teaching-delete'),
    path('teaching/<int:id>/update',TeachingUpdateAPIView.as_view(),name='teaching-update'),
    path('teaching/create/',TeachingCreateAPIView.as_view(),name='teaching-create'),
    path('teaching/<int:id>/edit',TeachingEditAPIView.as_view(),name='teaching-edit'),
    path('teaching/<int:id>/manage/',TeachingDeleteUpdateAPIView.as_view(),name='teaching-manage'),

    path('lessonlist/',LessonListAPIView.as_view(),name='lessonlist-list'),
    path('lessonlist/<int:id>/',LessonListDetailAPIView.as_view(),name='lessonlist-detail'),
    path('lessonlist/<int:id>/delete',LessonListDeleteAPIView.as_view(),name='lessonlist-delete'),
    path('lessonlist/<int:id>/update',LessonListUpdateAPIView.as_view(),name='lessonlist-update'),
    path('lessonlist/create/',LessonListCreateAPIView.as_view(),name='lessonlist-create'),
    path('lessonlist/<int:id>/edit',LessonListEditAPIView.as_view(),name='lessonlist-edit'),
    path('lessonlist/<int:id>/manage/',LessonListDeleteUpdateAPIView.as_view(),name='lessonlist-manage'),
]