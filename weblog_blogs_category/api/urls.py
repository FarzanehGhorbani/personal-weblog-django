from django.urls import path
from .views import (CategoryListAPIView,
                    CategoryDeleteAPIView,
                    CategoryUpdateAPIView,
                    CategoryCreateAPIView,
                    CategoryEditAPIView,
                    CategoryDeleteUpdateAPIView)
app_name = 'category-api'

urlpatterns =[
    path('',CategoryListAPIView.as_view(),name='category-list'),
    path('<int:id>/delete',CategoryDeleteAPIView.as_view(),name='category-delete'),
    path('<int:id>/update',CategoryUpdateAPIView.as_view(),name='category-update'),
    path('create/',CategoryCreateAPIView.as_view(),name='category-create'),
    path('<int:id>/edit',CategoryEditAPIView.as_view(),name='category-edit'),
    path('<int:id>/manage/',CategoryDeleteUpdateAPIView.as_view(),name='category-manage'),
]