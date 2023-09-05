from django.urls import path,include
from testapp.api.views import HydJobsCRUDCBV,PuneJobsCRUDCBV,DelhiJobsCRUDCBV
from rest_framework import routers
router=routers.DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV)
router.register('punejobsinfo',PuneJobsCRUDCBV)
router.register('delhijobsinfo',DelhiJobsCRUDCBV)

urlpatterns = [
    path('', include(router.urls)),
    
]