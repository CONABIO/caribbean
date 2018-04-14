from caribbean.models import MadmexCaribesample, MadmexTag, MadmexCountry
from caribbean.serializers import SampleSerializer, TagSerializer, CountrySerializer
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class SampleViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCaribesample.objects.all()
    serializer_class = SampleSerializer
    def get_queryset(self):
        if self.request.user.is_superuser:
            return FooModel.objects.all()
        return FooModel.objects.filter(owner=self.request.user)

class TagViewSet(viewsets.ModelViewSet):   
    queryset = MadmexTag.objects.all()
    serializer_class = TagSerializer


class CountryViewSet(viewsets.ModelViewSet):   
    queryset = MadmexCountry.objects.all()
    serializer_class = CountrySerializer

@login_required(login_url='/login/')
def map(request):
    return HttpResponse("Hello user %s." % request.user.id)