from rest_framework.serializers import ModelSerializer
from weblog_blogs_Tags.models import Tags

class TagListSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'



class TagDeleteSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class TagUpdateSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'


class TagCreateSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'

class TagEditSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'


class TagDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Tags
        fields='__all__'