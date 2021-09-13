from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from weblog_research.models import CurrentTopics,ResearchPartners,ResearchGrants


'''CurrentTopics'''
class CurrentTopicListSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields=('id','title')
        #for show special filed :
        #fields=('title')
        #fields=('id')


class CurrentTopicDetailSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'


class CurrentTopicDeleteSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'

class CurrentTopicUpdateSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'


class CurrentTopicCreateSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'


class CurrentTopicEditSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'


class CurrentTopicDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=CurrentTopics
        fields='__all__'


'''ResearchPartner'''
class ResearchPartnerListSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields=('id','full_name')
        #for show special filed :
        #fields=('full_name')
        #fields=('id')


class ResearchPartnerDetailSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'


class ResearchPartnerDeleteSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'

class ResearchPartnerUpdateSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'


class ResearchPartnerCreateSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'


class ResearchPartnerEditSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'


class ResearchPartnerDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model=ResearchPartners
        fields='__all__'

'''ResearchGrant'''
class ResearchGrantListSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields=('id','title')
        #for show special filed :
        #fields=('title')
        #fields=('id')


class ResearchGrantDetailSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'


class ResearchGrantDeleteSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'

class ResearchGrantUpdateSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'


class ResearchGrantCreateSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'

class ResearchGrantEditSerializer(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'


class ResearchGrantDeleteUpdateSerializ(ModelSerializer):
    class Meta:
        model=ResearchGrants
        fields='__all__'