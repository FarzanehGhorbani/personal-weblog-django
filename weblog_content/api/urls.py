from django.urls import path
from .views import (ContentListAPIView,
                    ContentDeleteAPIView,
                    ContentUpdateAPIView,
                    ContentCreateAPIView,
                    ContentEditAPIView,
                    ContentDeleteUpdateAPIView)
app_name = 'content-api'

urlpatterns =[
    path('',ContentListAPIView.as_view(),name='content-list'),
    path('<int:id>/delete',ContentDeleteAPIView.as_view(),name='content-delete'),
    path('<int:id>/update',ContentUpdateAPIView.as_view(),name='content-update'),
    path('create/',ContentCreateAPIView.as_view(),name='content-create'),
    path('<int:id>/edit',ContentEditAPIView.as_view(),name='content-edit'),
    path('<int:id>/manage/',ContentDeleteUpdateAPIView.as_view(),name='content-manage'),
]