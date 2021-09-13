from django.db.models import query
from django.db.models.query_utils import Q
from rest_framework import generics
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,    #request.user.is_staff == True
                                        IsAuthenticatedOrReadOnly)
from rest_framework.filters import ( SearchFilter,
                                    OrderingFilter)
from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import Serializer
from weblog_about_us.models import AboutUs
from .serializers import (
                        AboutUsLastSerializer,
                        AboutUsDeleteSerializer,
                        AboutUsUpdateSerializer,
                        AboutUsCreateSerializer,
                        AboutUsEditSerializer,
                        AboutUsDeleteUpdateSerializer
                        )
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class AboutUsLastAPIView(generics.ListAPIView): #read last
    queryset=AboutUs.objects.all().order_by('-id')[:1]
    serializer_class = AboutUsLastSerializer
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]




class AboutUsUpdateAPIView(generics.UpdateAPIView): #update
    queryset=AboutUs.objects.all()
    serializer_class = AboutUsUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
   

class AboutUsCreateAPIView(generics.CreateAPIView):#create
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]



class AboutUsEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=AboutUs.objects.all()
    serializer_class = AboutUsEditSerializer
    lookup_field='id'

class AboutUsDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=AboutUs.objects.all()
    serializer_class = AboutUsDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class AboutUsDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=AboutUs.objects.all()
    serializer_class = AboutUsDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

