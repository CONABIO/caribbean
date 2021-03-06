# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class MadmexCaribesample(models.Model):
    the_geom = models.GeometryField()
    added = models.DateTimeField()
    confidence = models.FloatField()
    st_area = models.FloatField()
    country = models.ForeignKey('MadmexCountry', models.DO_NOTHING)
    tag = models.ForeignKey('MadmexTag', models.DO_NOTHING)
    tag_editable = models.ForeignKey('MadmexTag', models.DO_NOTHING, related_name='tag_editable_interpreter')
    validated = models.BooleanField()
    class Meta:
        db_table = 'madmex_caribesample'

class MadmexCountry(models.Model):
    name = models.CharField(unique=True, max_length=100)
    the_geom = models.MultiPolygonField()
    added = models.DateTimeField()
    user_id = models.IntegerField()
    long_name = models.CharField(max_length=100)
    image = models.CharField(max_length=300)
    class Meta:
        db_table = 'madmex_country'

class MadmexTag(models.Model):
    scheme = models.CharField(max_length=50)
    value = models.CharField(max_length=150)
    numeric_code = models.IntegerField()
    color = models.CharField(max_length=7)

    class Meta:
        db_table = 'madmex_tag'
