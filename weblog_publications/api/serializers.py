from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_publications.models import Publications

class PublicationListSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields=('id','title')
        #for show special filed :
        #fields=('title')
        #fields=('id')



class PublicationDetailSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'


class PublicationDeleteSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'

class PublicationUpdateSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'


class PublicationCreateSerializer(ModelSerializer):
    class Meta:
        model=Publications
        exclude = ('owner',)


class PublicationEditSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'


class PublicationDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Publications
        fields='__all__'