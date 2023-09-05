from django.contrib import admin
from testapp.models import HydJobs,PuneJobs,delhiJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','address','email','phonenumber']

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','address','email','phonenumber']

class DelhiJobsAdmin(admin.ModelAdmin):
    list_display=['company','title','eligibility','address','email','phonenumber']

admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(PuneJobs,PunejobsAdmin)
admin.site.register(delhiJobs,DelhiJobsAdmin)