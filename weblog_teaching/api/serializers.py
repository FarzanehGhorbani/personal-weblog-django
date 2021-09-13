from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_teaching.models import Teaching,LessonList

'''LessonList'''
class LessonListSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields=('id','title')
        



class LessonListDetailSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'


class LessonListDeleteSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'

class LessonListUpdateSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'


class LessonListCreateSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'


class LessonListEditSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'


class LessonListDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=LessonList
        fields='__all__'

'''Teaching'''

class TeachingListSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields=('id','content')
        



class TeachingDetailSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'


class TeachingDeleteSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'

class TeachingUpdateSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'


class TeachingCreateSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'


class TeachingEditSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'


class TeachingDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=Teaching
        fields='__all__'