from django.contrib import admin
from career.models import CareerHistory

# Register your models here.
class CareerHistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname' ,'year', 'seasons_played')
    search_fields = ('name', 'surname')

admin.site.register(CareerHistory, CareerHistoryAdmin)