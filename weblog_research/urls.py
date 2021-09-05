from django.urls import path
from .views import research_page,ResearcherList,ResearcherDetailView

app_name='research'
urlpatterns=[
    path('',research_page,name='list'),
    path('researcher/',ResearcherList.as_view(),name='researcher_list'),
    path('researcher-<slug>/<name>/',ResearcherDetailView.as_view(),name='researcher_info')
]