from django.contrib import admin
from planes.models import Plane

class PlaneAdmin(admin.ModelAdmin):
    class Meta:
        model = Plane
    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time', )  # 'from_city'


admin.site.register(Plane, PlaneAdmin)