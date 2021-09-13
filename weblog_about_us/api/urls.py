from django.urls import path
from .views import (AboutUsLastAPIView,
                    AboutUsDeleteAPIView,
                    AboutUsUpdateAPIView,
                    AboutUsCreateAPIView,
                    AboutUsEditAPIView,
                    AboutUsDeleteUpdateAPIView)
app_name = 'about-us-api'

urlpatterns =[
    path('',AboutUsLastAPIView.as_view(),name='aboutus-list'),
    path('<int:id>/delete',AboutUsDeleteAPIView.as_view(),name='aboutus-delete'),
    path('<int:id>/update',AboutUsUpdateAPIView.as_view(),name='aboutus-update'),
    path('create/',AboutUsCreateAPIView.as_view(),name='aboutus-create'),
    path('<int:id>/edit',AboutUsEditAPIView.as_view(),name='aboutus-edit'),
    path('<int:id>/manage/',AboutUsDeleteUpdateAPIView.as_view(),name='aboutus-manage'),

]