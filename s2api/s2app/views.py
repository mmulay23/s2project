from django.shortcuts import render

from rest_framework import viewsets
from .models import mdlGeo,mdlPCategory, mdlProject, mdlPCharter, mdlPDeliverable
from .serializers import (mdlGeoSerializer, mdlPCategorySerializer, mdlProjectSerializer, 
            mdlPCharterSerializer,mdlPDeliverableSerializer)

# Create  views 
class mdlGeoViewSet(viewsets.ModelViewSet):
    serializer_class = mdlGeoSerializer
    queryset = mdlGeo.objects.all()


class mdlPCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = mdlPCategorySerializer
    queryset = mdlPCategory.objects.all()

class mdlProjectViewSet(viewsets.ModelViewSet):
    serializer_class = mdlProjectSerializer
    queryset = mdlProject.objects.all()

class mdlPCharterViewSet(viewsets.ModelViewSet):
    serializer_class = mdlPCharterSerializer
    queryset = mdlPCharter.objects.all()


class mdlPDeliverableViewSet(viewsets.ModelViewSet):
    serializer_class = mdlPDeliverableSerializer
    queryset = mdlPDeliverable.objects.all()

