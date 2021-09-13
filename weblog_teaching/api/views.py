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
from weblog_teaching.models import Teaching,LessonList
from .serializers import (TeachingListSerializer,
                        TeachingDetailSerializer,
                        TeachingDeleteSerializer,
                        TeachingUpdateSerializer,
                        TeachingCreateSerializer,
                        TeachingEditSerializer,
                        TeachingDeleteUpdateSerializer,
                        LessonListSerializer,
                        LessonListDetailSerializer,
                        LessonListDeleteSerializer,
                        LessonListUpdateSerializer,
                        LessonListCreateSerializer,
                        LessonListEditSerializer,
                        LessonListDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


'''LessonList'''
class LessonListAPIView(generics.ListAPIView): #read all
    #queryset=Teaching.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = LessonListSerializer
    search_fields = ('content','title')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or not self.request.user.is_anonymous:
            #superuser can see all teaching
            queryset=LessonList.objects.all()
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(content__icontains = query) |
                Q(title__icontains = query) | 
                Q(id__icontains = query) 
            ).distinct().order_by('-id')      

        return queryset          



class LessonListDetailAPIView(generics.RetrieveAPIView): #read
    queryset=LessonList.objects.all()
    serializer_class = LessonListDetailSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]



class LessonListUpdateAPIView(generics.UpdateAPIView): #update
    queryset=LessonList.objects.all()
    serializer_class = LessonListUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
   

class LessonListCreateAPIView(generics.CreateAPIView):#create
    queryset = LessonList.objects.all()
    serializer_class = LessonListCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]



class LessonListEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=LessonList.objects.all()
    serializer_class = LessonListEditSerializer
    lookup_field='id'

class LessonListDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=LessonList.objects.all()
    serializer_class = LessonListDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class LessonListDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=LessonList.objects.all()
    serializer_class = LessonListDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]



'''Teaching'''
class TeachingListAPIView(generics.ListAPIView): #read all
    #queryset=Teaching.objects.all()
    filter_backends = [DjangoFilterBackend]
    serializer_class = TeachingListSerializer
    search_fields = ('content')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or not self.request.user.is_anonymous:
            #superuser can see all teaching
            queryset=Teaching.objects.all()
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(content__icontains = query) |
                Q(id__icontains = query) 
            ).distinct().order_by('-id')      

        return queryset          



class TeachingDetailAPIView(generics.RetrieveAPIView): #read
    queryset=Teaching.objects.all()
    serializer_class = TeachingDetailSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]



class TeachingUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Teaching.objects.all()
    serializer_class = TeachingUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
   

class TeachingCreateAPIView(generics.CreateAPIView):#create
    queryset = Teaching.objects.all()
    serializer_class = TeachingCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]



class TeachingEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Teaching.objects.all()
    serializer_class = TeachingEditSerializer
    lookup_field='id'

class TeachingDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Teaching.objects.all()
    serializer_class = TeachingDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class TeachingDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Teaching.objects.all()
    serializer_class = TeachingDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

