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
from weblog_publications.models import Publications
from .serializers import (PublicationListSerializer,
                        PublicationDetailSerializer,
                        PublicationDeleteSerializer,
                        PublicationUpdateSerializer,
                        PublicationCreateSerializer,
                        PublicationEditSerializer,
                        PublicationDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class PublicationListAPIView(generics.ListAPIView): #read all
    #queryset=Publications.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = PublicationListSerializer
    ordering_fields=('publish_date',)
    filter_fields = ('title','content','writer','owner__username')
    search_fields = ('title','content','writer','owner__username')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser:
            #superuser can see all books
            queryset=Publications.objects.all()
        elif not self.request.user.is_anonymous:
            #otherwise every user can see this book
            queryset = Publications.objects.filter(owner = self.request.user)
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains = query) |
                Q(content__icontains = query) |
                Q(writer__icontains = query) |
                Q(id__icontains = query) |
                Q(owner__first_name__icontains = query) |
                Q(owner__last_name__icontains = query) |
                Q(owner__username__icontains = query) 
            ).distinct().order_by('-publish_date')      

        return queryset          



class PublicationDetailAPIView(generics.RetrieveAPIView): #read
    queryset=Publications.objects.all()
    serializer_class = PublicationDetailSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]



class PublicationUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Publications.objects.all()
    serializer_class = PublicationUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    def perform_update(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update

class PublicationCreateAPIView(generics.CreateAPIView):#create
    queryset = Publications.objects.all()
    serializer_class = PublicationCreateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_create(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update


class PublicationEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Publications.objects.all()
    serializer_class = PublicationEditSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

class PublicationDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Publications.objects.all()
    serializer_class = PublicationDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class PublicationDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Publications.objects.all()
    serializer_class = PublicationDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]


