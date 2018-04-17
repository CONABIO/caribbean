from rest_framework import serializers

from caribbean.models import MadmexCaribesample, MadmexTag, MadmexCountry

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MadmexCaribesample
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MadmexTag
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MadmexCountry
        fields = ('id','name','long_name','image')