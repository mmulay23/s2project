from rest_framework import serializers
from .models import mdlGeo, mdlPCategory, mdlProject, mdlPCharter, mdlPDeliverable

class mdlGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdlGeo
        fields=['id','country','region']

class mdlPCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = mdlPCategory
        fields=['id','category','subcategory']

class mdlProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = mdlProject
        fields =['id','project','subcategory','country','year','budget','outcome']


class mdlPCharterSerializer(serializers.ModelSerializer):
    class Meta: 
        model =mdlPCharter
        fields=['id','project_phase','project_owner','project','description','start_date',
                'end_date', 'budget', 'human_resources','stage']


class mdlPDeliverableSerializer(serializers.ModelSerializer):
    class Meta: 
        model =mdlPDeliverable
        fields=['id','deliverable_name','project_phase','content_type','title','authors',
                    'published_date','description','url' ]

