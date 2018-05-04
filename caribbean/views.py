from caribbean.models import MadmexCaribesample, MadmexTag, MadmexCountry
from caribbean.serializers import SampleSerializer, TagSerializer, CountrySerializer
from rest_framework import viewsets
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import requests

class SampleViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCaribesample.objects.all()
    serializer_class = SampleSerializer
    def get_queryset(self):
        print(self.request.user.pk)
        if self.request.user.is_superuser:
           return MadmexCaribesample.objects.all()
        elif self.request.user.pk is not None:
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
def count(request):
    print("Hello")
    if request.user.is_superuser:
        validated = MadmexCaribesample.objects.filter(validated=True).count()
        remaining = MadmexCaribesample.objects.filter(validated=False).count()
    else:
        validated = MadmexCaribesample.objects.filter(country__user_id=request.user.pk, validated=True).count()
        remaining = MadmexCaribesample.objects.filter(country__user_id=request.user.pk, validated=False).count()
    result = {'validated':validated,
              'remaining':remaining}
    return JsonResponse(result)


@login_required(login_url='/login/')
def map(request):
    if request.user.is_superuser:
      path = 'https://raw.githubusercontent.com/hjnilsson/country-flags/master/png250px/mx.png'
      name = 'Admin'
    else:
      path = MadmexCountry.objects.get(user_id=request.user.pk).image
      name = MadmexCountry.objects.get(user_id=request.user.pk).long_name
    countries = json.dumps(CountrySerializer(MadmexCountry.objects.all(), many=True).data)
    tags_list = TagSerializer(MadmexTag.objects.all(), many=True).data
    tags = json.dumps(tags_list)
    return TemplateResponse(request, 'map.html', {'path':path, 
                                                  'name':name,
                                                  'countries':countries,
                                                  'tags':tags,
                                                  'tags_list':tags_list})