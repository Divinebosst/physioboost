from django.contrib import admin
from . models import Season

# Register your models here.
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'started_on')
	
admin.site.register(Season, SeasonAdmin)
