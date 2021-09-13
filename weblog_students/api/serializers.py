from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_students.models import Students

class StudentListSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields=('id','full_name')
        #for show special filed :
        #fields=('title')
        #fields=('id')



class StudentDetailSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'


class StudentDeleteSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'

class StudentUpdateSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'


class StudentCreateSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'

class StudentEditSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'


class StudentDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Students
        fields='__all__'