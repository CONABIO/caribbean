from caribbean.models import MadmexCaribesample, MadmexTag, MadmexCountry
from caribbean.serializers import SampleSerializer, TagSerializer, CountrySerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
import requests

class SampleViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCaribesample.objects.all()
    serializer_class = SampleSerializer
    def get_queryset(self):
        print(self.request.user.pk)
        if self.request.user.pk is not None:
           return MadmexCaribesample.objects.filter(country__user_id=self.request.user.pk)
        else:
           return MadmexCaribesample.objects.none()

class TagViewSet(viewsets.ModelViewSet):   
    queryset = MadmexTag.objects.all()
    serializer_class = TagSerializer


class CountryViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCountry.objects.all()
    serializer_class = CountrySerializer

@login_required(login_url='/login/')
def map(request):
    return TemplateResponse(request, 'map.html', {})