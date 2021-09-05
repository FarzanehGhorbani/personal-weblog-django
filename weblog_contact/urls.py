from django.urls import path
from .views import contact_page,contactway_contact

app_name='contact'
urlpatterns = [
    path('', contact_page,name='contact'),
    path('contactway_contact/', contactway_contact,name='contact_way'),
]
