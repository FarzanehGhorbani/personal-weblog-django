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
from weblog_blogs_category.models import Categories
from .serializers import (
                        CategoryListSerializer,
                        CategoryDeleteSerializer,
                        CategoryUpdateSerializer,
                        CategoryCreateSerializer,
                        CategoryEditSerializer,
                        CategoryDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryListAPIView(generics.ListAPIView): #read all
    #queryset=Blogs.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = CategoryListSerializer
    ordering_fields=('id',)
    filter_fields = ('title','name')
    search_fields = ('title','name')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or not self.request.user.is_anonymous:
            #superuser can see all blogs
            queryset=Categories.objects.all()
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains = query) |
                Q(name__icontains = query) |
                Q(id__icontains = query) 
            ).distinct().order_by('-id')      

        return queryset          





class CategoryUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Categories.objects.all()
    serializer_class = CategoryUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    

class CategoryCreateAPIView(generics.CreateAPIView):#create
    queryset = Categories.objects.all()
    serializer_class = CategoryCreateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]


class CategoryEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Categories.objects.all()
    serializer_class = CategoryEditSerializer
    lookup_field='id'

class CategoryDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Categories.objects.all()
    serializer_class = CategoryDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    


class CategoryDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Categories.objects.all()
    serializer_class = CategoryDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
