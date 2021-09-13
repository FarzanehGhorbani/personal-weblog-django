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
from weblog_research.models import (CurrentTopics,
                                    ResearchGrants,
                                    ResearchPartners)
from .serializers import (CurrentTopicListSerializer,
                        CurrentTopicDetailSerializer,
                        CurrentTopicDeleteSerializer,
                        CurrentTopicUpdateSerializer,
                        CurrentTopicCreateSerializer,
                        CurrentTopicEditSerializer,
                        CurrentTopicDeleteUpdateSerializer,
                        ResearchGrantListSerializer,
                        ResearchGrantDetailSerializer,
                        ResearchGrantDeleteSerializer,
                        ResearchGrantUpdateSerializer,
                        ResearchGrantCreateSerializer,
                        ResearchGrantEditSerializer,
                        ResearchGrantDeleteUpdateSerializ,
                        ResearchPartnerListSerializer,
                        ResearchPartnerDetailSerializer,
                        ResearchPartnerDeleteSerializer,
                        ResearchPartnerUpdateSerializer,
                        ResearchPartnerCreateSerializer,
                        ResearchPartnerEditSerializer,
                        ResearchPartnerDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class ResearchPartnerListAPIView(generics.ListAPIView): #read all
    #queryset=ResearchPartners.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = ResearchPartnerListSerializer
    ordering_fields=('created_on','active')
    filter_fields = ('full_name','rule','description','blogs','created_on','active')
    search_fields = ('full_name','rule','description','blogs','created_on','active')  
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_anonymous:
            #superuser can see all books
            queryset=ResearchPartners.objects.all()
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
                Q(description__icontains = query) |
                Q(id__icontains = query) |
                Q(blog__icontains = query) |
                Q(active_iexact = query) 
            ).distinct().order_by('-created_on')      

        return queryset          



class ResearchPartnerDetailAPIView(generics.RetrieveAPIView): #read
    #queryset=ResearchPartners.objects.all()
    serializer_class = ResearchPartnerDetailSerializer
    lookup_field='id'
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_authenticated:
            #superuser can see all CurrentTopics
            queryset=ResearchPartners.objects.all()
        else:
            return None

        return queryset

# class ResearchPartnerDeleteAPIView(generics.DestroyAPIView):#delete
#     queryset=ResearchPartners.objects.all()
#     serializer_class = ResearchPartnerDeleteSerializer
#     lookup_field='id'

class ResearchPartnerUpdateAPIView(generics.UpdateAPIView): #update
    queryset=ResearchPartners.objects.all()
    serializer_class = ResearchPartnerUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    def perform_update(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update

class ResearchPartnerCreateAPIView(generics.CreateAPIView):#create
    queryset = ResearchPartners.objects.all()
    serializer_class = ResearchPartnerCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update


class ResearchPartnerEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=ResearchPartners.objects.all()
    serializer_class = ResearchPartnerEditSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

class ResearchPartnerDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=ResearchPartners.objects.all()
    serializer_class = ResearchPartnerDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class ResearchPartnerDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=ResearchPartners.objects.all()
    serializer_class = ResearchPartnerDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

''''''
class ResearchGrantListAPIView(generics.ListAPIView): #read all
    queryset=ResearchGrants.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = ResearchGrantListSerializer
    ordering_fields=('created_on')
    filter_fields = ('title','company','rule','created_on')
    search_fields = ('title','company','rule','created_on')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser:
            #superuser can see all books
            queryset=ResearchGrants.objects.all()
        elif not self.request.user.is_anonymous:
            #otherwise every user can see this book
            queryset = ResearchGrants.objects.filter(owner = self.request.user)
        else:
            return None
        #custom search.It is not related to rest_framework
        query = self.request.GET.get('q')
        #query = some thing


        if query:
            #if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains = query) |
                Q(company__icontains = query) |
                Q(rule__icontains = query) |
                Q(id__icontains = query) 
            ).distinct().order_by('-created_on')      

        return queryset          



class ResearchGrantDetailAPIView(generics.RetrieveAPIView): #read
    #queryset=ResearchGrants.objects.all()
    serializer_class = ResearchGrantDetailSerializer
    lookup_field='id'
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_authenticated:
            #superuser can see all CurrentTopics
            queryset=ResearchGrants.objects.all()
        else:
            return None

        return queryset

# class ResearchGrantDeleteAPIView(generics.DestroyAPIView):#delete
#     queryset=ResearchGrants.objects.all()
#     serializer_class = ResearchGrantDeleteSerializer
#     lookup_field='id'

class ResearchGrantUpdateAPIView(generics.UpdateAPIView): #update
    queryset=ResearchGrants.objects.all()
    serializer_class = ResearchGrantUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    def perform_update(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update

class ResearchGrantCreateAPIView(generics.CreateAPIView):#create
    queryset = ResearchGrants.objects.all()
    serializer_class = ResearchGrantCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update


class ResearchGrantEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=ResearchGrants.objects.all()
    serializer_class = ResearchGrantEditSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

class ResearchGrantDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=ResearchGrants.objects.all()
    serializer_class = ResearchGrantDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class ResearchGrantDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=ResearchGrants.objects.all()
    serializer_class = ResearchGrantDeleteUpdateSerializ
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]


'''CurrentTopics'''
class CurrentTopicListAPIView(generics.ListAPIView): #read all
    #queryset=CurrentTopics.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = CurrentTopicListSerializer
    ordering_fields=('created_on','active')
    filter_fields = ('title','content','created_on','active')
    search_fields = ('title','content','created_on','active')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_authenticated:
            #superuser can see all CurrentTopics
            queryset=CurrentTopics.objects.all()
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
                Q(id__icontains = query)| 
                Q(active__iexact = query) 
                ).distinct().order_by('-created_on')      

        return queryset          



class CurrentTopicDetailAPIView(generics.RetrieveAPIView): #read
    #queryset=CurrentTopics.objects.all()
    serializer_class = CurrentTopicDetailSerializer
    lookup_field='id'
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser or self.request.user.is_authenticated:
            #superuser can see all CurrentTopics
            queryset=CurrentTopics.objects.all()
        else:
            return None

        return queryset

# class CurrentTopicDeleteAPIView(generics.DestroyAPIView):#delete
#     queryset=CurrentTopics.objects.all()
#     serializer_class = CurrentTopicDeleteSerializer
#     lookup_field='id'

class CurrentTopicUpdateAPIView(generics.UpdateAPIView): #update
    queryset=CurrentTopics.objects.all()
    serializer_class = CurrentTopicUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    def perform_update(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update

class CurrentTopicCreateAPIView(generics.CreateAPIView):#create
    queryset = CurrentTopics.objects.all()
    serializer_class = CurrentTopicCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update


class CurrentTopicEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=CurrentTopics.objects.all()
    serializer_class = CurrentTopicEditSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]


class CurrentTopicDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=CurrentTopics.objects.all()
    serializer_class = CurrentTopicDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class CurrentTopicDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=CurrentTopics.objects.all()
    serializer_class = CurrentTopicDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

