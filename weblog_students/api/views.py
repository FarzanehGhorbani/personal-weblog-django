from django.db.models.query import prefetch_related_objects
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
from weblog_students.models import Students
from .serializers import (StudentListSerializer,
                        StudentDetailSerializer,
                        StudentDeleteSerializer,
                        StudentUpdateSerializer,
                        StudentCreateSerializer,
                        StudentEditSerializer,
                        StudentDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class StudentListAPIView(generics.ListAPIView): #read all
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = StudentListSerializer
    ordering_fields=('created_on',)
    filter_fields = ('full_name','rule','description','active')
    search_fields = ('full_name','rule','description','active')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_anonymous:
            #superuser can see all books
            queryset=Students.objects.all()
        
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(full_name__icontains = query) |
                Q(rule__icontains = query) |
                Q(description__icontains = query) 
            ).distinct().order_by('-created_on')      

        return queryset          



class StudentDetailAPIView(generics.RetrieveAPIView): #read
    queryset=Students.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field='id'
    prefetch_related_objects=[OwnerCanManagerOrReadOnly,IsAuthenticated]

class StudentUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Students.objects.all()
    serializer_class = StudentUpdateSerializer
    lookup_field='id'
    prefetch_related_objects=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    

class StudentCreateAPIView(generics.CreateAPIView):#create
    queryset = Students.objects.all()
    serializer_class = StudentCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]



class StudentEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Students.objects.all()
    serializer_class = StudentEditSerializer
    lookup_field='id'
    prefetch_related_objects=[OwnerCanManagerOrReadOnly,IsAuthenticated]

class StudentDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Students.objects.all()
    serializer_class = StudentDeleteSerializer
    lookup_field='id'
    prefetch_related_objects=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class StudentDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Students.objects.all()
    serializer_class = StudentDeleteUpdateSerializer
    lookup_field='id'
    prefetch_related_objects=[OwnerCanManagerOrReadOnly,IsAuthenticated]


