from django.urls import path
from .views import (BlogListAPIView,
                    BlogDetailAPIView,
                    BlogDeleteAPIView,
                    BlogUpdateAPIView,
                    BlogCreateAPIView,
                    BlogEditAPIView,
                    BlogDeleteUpdateAPIView)
app_name = 'blog-api'

urlpatterns =[
    path('',BlogListAPIView.as_view(),name='blog-list'),
    path('<int:id>/',BlogDetailAPIView.as_view(),name='blog-detail'),
    path('<int:id>/delete',BlogDeleteAPIView.as_view(),name='blog-delete'),
    path('<int:id>/update',BlogUpdateAPIView.as_view(),name='blog-update'),
    path('create/',BlogCreateAPIView.as_view(),name='blog-create'),
    path('<int:id>/edit',BlogEditAPIView.as_view(),name='blog-edit'),
    path('<int:id>/manage/',BlogDeleteUpdateAPIView.as_view(),name='blog-manage'),
]