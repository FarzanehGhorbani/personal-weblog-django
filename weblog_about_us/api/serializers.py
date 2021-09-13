from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_about_us.models import AboutUs

'''AboutUs'''
class AboutUsLastSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'


class AboutUsDeleteSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'

class AboutUsUpdateSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'


class AboutUsCreateSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'


class AboutUsEditSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'


class AboutUsDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=AboutUs
        fields='__all__'

