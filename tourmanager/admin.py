from django.contrib import admin
from tourmanager.models import Regions, Destinations, Tours, TourData

class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'map_location')



admin.site.register(Regions, RegionsAdmin)
admin.site.register(Destinations)
admin.site.register(Tours)
admin.site.register(TourData)