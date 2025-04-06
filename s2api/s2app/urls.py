from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (mdlGeoViewSet, mdlPCategoryViewSet, mdlProjectViewSet,
                    mdlPCharterViewSet, mdlPDeliverableViewSet)

router = DefaultRouter()
router.register(r'country', mdlGeoViewSet)
router.register(r'subcategory', mdlPCategoryViewSet)
router.register(r'project', mdlProjectViewSet)
router.register(r'project_phase', mdlPCharterViewSet)
router.register(r'deliverable_name', mdlPDeliverableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]