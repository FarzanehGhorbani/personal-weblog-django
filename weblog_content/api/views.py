from rest_framework import generics
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,    #request.user.is_staff == True
                                        IsAuthenticatedOrReadOnly)
from rest_framework.filters import ( SearchFilter,
                                    OrderingFilter)
from rest_framework.exceptions import PermissionDenied
from rest_framework.serializers import Serializer
from weblog_content.models import Content
from .serializers import (ContentListSerializer,
                        ContentDeleteSerializer,
                        ContentUpdateSerializer,
                        ContentCreateSerializer,
                        ContentEditSerializer,
                        ContentDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ContentListAPIView(generics.ListAPIView): #read last
    queryset=Content.objects.all().order_by('-id')[:1]
    serializer_class = ContentListSerializer
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]




class ContentUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Content.objects.all()
    serializer_class = ContentUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    
class ContentCreateAPIView(generics.CreateAPIView):#create
    queryset = Content.objects.all()
    serializer_class = ContentCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]


class ContentEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Content.objects.all()
    serializer_class = ContentEditSerializer
    lookup_field='id'

class ContentDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Content.objects.all()
    serializer_class = ContentDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class ContentDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Content.objects.all()
    serializer_class = ContentDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

