from django.urls import path
from .views import (PublicationListAPIView,
                    PublicationDetailAPIView,
                    PublicationDeleteAPIView,
                    PublicationUpdateAPIView,
                    PublicationCreateAPIView,
                    PublicationEditAPIView,
                    PublicationDeleteUpdateAPIView)

app_name = 'publication-api'

urlpatterns =[
    path('',PublicationListAPIView.as_view(),name='publication-list'),
    path('<int:id>/',PublicationDetailAPIView.as_view(),name='publication-detail'),
    path('<int:id>/delete',PublicationDeleteAPIView.as_view(),name='publication-delete'),
    path('<int:id>/update',PublicationUpdateAPIView.as_view(),name='publication-update'),
    path('create/',PublicationCreateAPIView.as_view(),name='publication-create'),
    path('<int:id>/edit',PublicationEditAPIView.as_view(),name='publication-edit'),
    path('<int:id>/manage/',PublicationDeleteUpdateAPIView.as_view(),name='publication-manage'),
]