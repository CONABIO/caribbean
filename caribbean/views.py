from caribbean.models import MadmexCaribesample
from caribbean.serializers import SampleSerializer
from rest_framework import viewsets

class SampleViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCaribesample.objects.all()
    serializer_class = SampleSerializer