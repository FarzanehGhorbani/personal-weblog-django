from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_content.models import Content

class ContentListSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'


class ContentDeleteSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'

class ContentUpdateSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'


class ContentCreateSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'


class ContentEditSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'


class ContentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Content
        fields='__all__'