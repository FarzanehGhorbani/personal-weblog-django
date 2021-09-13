from rest_framework.serializers import ModelSerializer
from weblog_blogs_category.models import Categories

class CategoryListSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'



class CategoryDeleteSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'

class CategoryUpdateSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'


class CategoryCreateSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'

class CategoryEditSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'


class CategoryDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'