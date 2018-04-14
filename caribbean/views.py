from caribbean.models import MadmexCaribesample, MadmexTag, MadmexCountry
from caribbean.serializers import SampleSerializer, TagSerializer, CountrySerializer
from rest_framework import viewsets

class SampleViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCaribesample.objects.all()
    serializer_class = SampleSerializer

class TagViewSet(viewsets.ModelViewSet):   
    queryset = MadmexTag.objects.all()
    serializer_class = TagSerializer

class CountryViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCountry.objects.all()
    serializer_class = CountrySerializer