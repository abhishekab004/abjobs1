from rest_framework.serializers import ModelSerializer
from testapp.models import HydJobs,PuneJobs,delhiJobs
class HydJobsSerializers(ModelSerializer):
    class Meta:
        model=HydJobs
        fields='__all__'

class PuneJobsSerializers(ModelSerializer):
    class Meta:
        model=PuneJobs
        fields='__all__'

class DelhiJobsSerializers(ModelSerializer):
    class Meta:
        model=delhiJobs
        fields='__all__'