from django.urls import path
from .views import (CurrentTopicListAPIView,
                    CurrentTopicDetailAPIView,
                    CurrentTopicDeleteAPIView,
                    CurrentTopicUpdateAPIView,
                    CurrentTopicCreateAPIView,
                    CurrentTopicEditAPIView,
                    CurrentTopicDeleteUpdateAPIView,
                    
                    ResearchGrantListAPIView,
                    ResearchGrantDetailAPIView,
                    ResearchGrantDeleteAPIView,
                    ResearchGrantUpdateAPIView,
                    ResearchGrantCreateAPIView,
                    ResearchGrantEditAPIView,
                    ResearchGrantDeleteUpdateAPIView,
                    
                    ResearchPartnerListAPIView,
                    ResearchPartnerDetailAPIView,
                    ResearchPartnerDeleteAPIView,
                    ResearchPartnerUpdateAPIView,
                    ResearchPartnerCreateAPIView,
                    ResearchPartnerEditAPIView,
                    ResearchPartnerDeleteUpdateAPIView)
app_name = 'research-api'

urlpatterns =[
    path('currenttopic/',CurrentTopicListAPIView.as_view(),name='currenttopic-list'),
    path('currenttopic/<int:id>/',CurrentTopicDetailAPIView.as_view(),name='currenttopic-detail'),
    path('currenttopic/<int:id>/delete',CurrentTopicDeleteAPIView.as_view(),name='currenttopic-delete'),
    path('currenttopic/<int:id>/update',CurrentTopicUpdateAPIView.as_view(),name='currenttopic-update'),
    path('currenttopic/create/',CurrentTopicCreateAPIView.as_view(),name='currenttopic-create'),
    path('currenttopic/<int:id>/edit',CurrentTopicEditAPIView.as_view(),name='currenttopic-edit'),
    path('currenttopic/<int:id>/manage/',CurrentTopicDeleteUpdateAPIView.as_view(),name='currenttopic-manage'),

    path('researchgrant/',ResearchGrantListAPIView.as_view(),name='researchgrant-list'),
    path('researchgrant/<int:id>/',ResearchGrantDetailAPIView.as_view(),name='researchgrant-detail'),
    path('researchgrant/<int:id>/delete',ResearchGrantDeleteAPIView.as_view(),name='researchgrant-delete'),
    path('researchgrant/<int:id>/update',ResearchGrantUpdateAPIView.as_view(),name='researchgrant-update'),
    path('researchgrant/create/',ResearchGrantCreateAPIView.as_view(),name='researchgrant-create'),
    path('researchgrant/<int:id>/edit',ResearchGrantEditAPIView.as_view(),name='researchgrant-edit'),
    path('researchgrant/<int:id>/manage/',ResearchGrantDeleteUpdateAPIView.as_view(),name='researchgrant-manage'),

    path('researchpartner/',ResearchPartnerListAPIView.as_view(),name='researchpartner-list'),
    path('researchpartner/<int:id>/',ResearchPartnerDetailAPIView.as_view(),name='researchpartner-detail'),
    path('researchpartner/<int:id>/delete',ResearchPartnerDeleteAPIView.as_view(),name='researchpartner-delete'),
    path('researchpartner/<int:id>/update',ResearchPartnerUpdateAPIView.as_view(),name='researchpartner-update'),
    path('researchpartner/create/',ResearchPartnerCreateAPIView.as_view(),name='researchpartner-create'),
    path('researchpartner/<int:id>/edit',ResearchPartnerEditAPIView.as_view(),name='researchpartner-edit'),
    path('researchpartner/<int:id>/manage/',ResearchPartnerDeleteUpdateAPIView.as_view(),name='researchpartner-manage'),
]