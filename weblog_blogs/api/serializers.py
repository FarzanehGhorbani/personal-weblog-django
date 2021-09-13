from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_blogs.models import Blogs

class BlogListSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields=('id','title')
        #for show special filed :
        #fields=('title')
        #fields=('id')



class BlogDetailSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'


class BlogDeleteSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'

class BlogUpdateSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'


class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        exclude = ('owner',)


class BlogEditSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'


class BlogDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Blogs
        fields='__all__'