from rest_framework import viewsets
from testapp.models import HydJobs,PuneJobs,delhiJobs
from testapp.api.serializers import HydJobsSerializers,PuneJobsSerializers,DelhiJobsSerializers
class HydJobsCRUDCBV(viewsets.ModelViewSet):
    queryset=HydJobs.objects.all()
    serializer_class=HydJobsSerializers

class PuneJobsCRUDCBV(viewsets.ModelViewSet):
    queryset=PuneJobs.objects.all()
    serializer_class=PuneJobsSerializers

class DelhiJobsCRUDCBV(viewsets.ModelViewSet):
    queryset=delhiJobs.objects.all()
    serializer_class=DelhiJobsSerializers