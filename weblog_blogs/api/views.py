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
from weblog_blogs.models import Blogs
from .serializers import (BlogListSerializer,
                        BlogDetailSerializer,
                        BlogDeleteSerializer,
                        BlogUpdateSerializer,
                        BlogCreateSerializer,
                        BlogEditSerializer,
                        BlogDeleteUpdateSerializer)
from .permissions import OwnerCanManagerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class BlogListAPIView(generics.ListAPIView): #read all
    #queryset=Blogs.objects.all()
    filter_backends = [SearchFilter,OrderingFilter,DjangoFilterBackend]
    serializer_class = BlogListSerializer
    ordering_fields=('publish_date',)
    filter_fields = ('title','content','owner__username')
    search_fields = ('title','content','owner__username')   
    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_superuser:
            #superuser can see all blogs
            queryset=Blogs.objects.all()
        elif not self.request.user.is_anonymous:
            #otherwise every user can see this blog
            queryset = Blogs.objects.filter(owner = self.request.user)
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
                Q(id__icontains = query) |
                Q(owner__first_name__icontains = query) |
                Q(owner__last_name__icontains = query) |
                Q(owner__username__icontains = query) 
            ).distinct().order_by('-publish_date')      

        return queryset          



class BlogDetailAPIView(generics.RetrieveAPIView): #read
    queryset=Blogs.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

# class BlogDeleteAPIView(generics.DestroyAPIView):#delete
#     queryset=Blogs.objects.all()
#     serializer_class = BlogDeleteSerializer
#     lookup_field='id'

class BlogUpdateAPIView(generics.UpdateAPIView): #update
    queryset=Blogs.objects.all()
    serializer_class = BlogUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]
    def perform_update(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update

class BlogCreateAPIView(generics.CreateAPIView):#create
    queryset = Blogs.objects.all()
    serializer_class = BlogCreateSerializer
    lookup_field='id'
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        Serializer.save(owner=self.request.user)
        #we can send email here and etc.this is email send when serializer update


class BlogEditAPIView(generics.RetrieveUpdateAPIView): # read or update
    queryset=Blogs.objects.all()
    serializer_class = BlogEditSerializer
    lookup_field='id'

class BlogDeleteAPIView(generics.RetrieveDestroyAPIView):#delete or read
    queryset=Blogs.objects.all()
    serializer_class = BlogDeleteSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

    def perform_destroy(self, serializer):
        if serializer.owner != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()


class BlogDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):#delete or read or update
    queryset=Blogs.objects.all()
    serializer_class = BlogDeleteUpdateSerializer
    lookup_field='id'
    permission_classes=[OwnerCanManagerOrReadOnly,IsAuthenticated]

'''

for show json in terminal :
     pip install httpie

in comand :  http url_of_page


Create url: open teminal and type this url. Note that httpie must be installed.

$ http -a <USERNAME>:<PASSWORD> http://127.0.0.1:8000/api/create/ title='<YOUR_TITLE>' content='<YOUR_CONTENT>' owner=<OWNER_ID>

Delete url: open teminal and type this url.

$ http -a <USERNAME>:<PASSWORD> DELETE http://127.0.0.1:8000/api/<POST_ID>/delete

Update url: open teminal and type this url.

`$ http -a : PUT http://127.0.0.1:8000/api/<POST_ID>/edit title='<YOUR_TITLE>' content='<YOUR_CONTENT>' owner=<OWNER_ID>``

'''


'''
for add blog 
from weblog_blogs.models import Blogs
from weblog_blogs.api.serializers import BlogDetailSerializer
data={
    "title": "زندگی دانشجویی",
    "writer": "فرزانه قربانی",
    "publish_date": "2021-09-09",
    "content":"this is for test",
}

item=BlogDetailSerializer(data=data)

if item.is_valid():
    item.save()
else:
    print(item.errors)

'''