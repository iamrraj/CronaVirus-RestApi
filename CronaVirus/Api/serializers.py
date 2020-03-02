from rest_framework import serializers
from ..models import CronaVirus, Cities, Area, News, Remours
from django.contrib.auth.models import User


class CronaVirusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronaVirus
        exclude = ['id']
        # fields = ['currentConfirmedCount', 'confirmCount', 'suspectedCount', 'curedCount', 'deadCount', 'seriousCount', 'currentConfirmedIncr',
        #           'confirmIncr', 'suspectedIncr', 'curedIncr', 'seriousIncr', 'deadIncr', 'updateTime', 'note1', 'note2', 'note3']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ResmoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remours
        fields = "__all__"


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        exclude = ['cities', 'lat', 'lon']
