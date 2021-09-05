from django.urls import path
from .views import publications_page,book_detail
app_name='publications'

urlpatterns=[
    path('',publications_page,name='list'),
    path('books-<slug>/<name>/',book_detail,name='info')
]