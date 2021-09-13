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
from weblog_blogs_Tags.models import Tags
from .serializers import (
                        TagListSerializer,
                        TagDeleteSerializer,
                        TagUpdateSerializer,
                        TagCreateSerializer,
                        TagEditSerializer,
                        TagDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class TagListAPIView(generics.ListAPIView): #read all
    #queryset=Blogs.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = TagListSerializer
    ordering_fields=('id',)
    filter_fields = ('title','slug','active')
    search_fields = ('title','slug','active')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or not self.request.user.is_anonymous:
            #superuser can see all blogs
            queryset=Tags.objects.all()
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains = query) |
                Q(slug__icontains = query) |
                Q(id__icontains = query) 
            ).distinct().order_by('-timestamp')      

        return queryset          





class TagUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Tags.objects.all()
    serializer_class = TagUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    

class TagCreateAPIView(generics.CreateAPIView):#create
    queryset = Tags.objects.all()
    serializer_class = TagCreateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]


class TagEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Tags.objects.all()
    serializer_class = TagEditSerializer
    lookup_field='id'

class TagDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Tags.objects.all()
    serializer_class = TagDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    


class TagDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Tags.objects.all()
    serializer_class = TagDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
