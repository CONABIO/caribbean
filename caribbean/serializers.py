from rest_framework import serializers

from caribbean.models import MadmexCaribesample

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MadmexCaribesample
        fields = '__all__'