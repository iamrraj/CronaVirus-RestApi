from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from . import serializers
from ..models import CronaVirus, Area, Cities, News, Remours
from rest_framework.response import Response
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CronaView(ListAPIView):
    queryset = CronaVirus.objects.order_by('-pk')[:1]
    serializer_class = serializers.CronaVirusSerializer


class RemourView(ListAPIView):
    queryset = Remours.objects.all()
    serializer_class = serializers.ResmoutSerializer


class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'provinceId': ['in', 'exact'],
        'provinceName': ['icontains'],
    }




class AreaView(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'locationId': ['exact', 'in', ],
        'continentName': ['exact', 'in', 'icontains'],
        'country': ['exact', 'in', 'icontains'],
        'provinceName': ['exact', 'in', 'icontains'],
    }
