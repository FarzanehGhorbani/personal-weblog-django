from django.urls import path
from .views import (TagListAPIView,
                    TagDeleteAPIView,
                    TagUpdateAPIView,
                    TagCreateAPIView,
                    TagEditAPIView,
                    TagDeleteUpdateAPIView)
app_name = 'tag-api'

urlpatterns =[
    path('',TagListAPIView.as_view(),name='tag-list'),
    path('<int:id>/delete',TagDeleteAPIView.as_view(),name='tag-delete'),
    path('<int:id>/update',TagUpdateAPIView.as_view(),name='tag-update'),
    path('create/',TagCreateAPIView.as_view(),name='tag-create'),
    path('<int:id>/edit',TagEditAPIView.as_view(),name='tag-edit'),
    path('<int:id>/manage/',TagDeleteUpdateAPIView.as_view(),name='tag-manage'),
]