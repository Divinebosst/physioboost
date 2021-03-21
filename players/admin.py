from django.contrib import admin
from . models import Player

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'nationality', 'date_of_birth', 'age', 'height', 'weight','preferred_foot', 'position', 'jersey_number', 'strengths' , 'weaknesses','club', 'status')
    search_fields = ('name', 'surname', 'club')
    
admin.site.register(Player, PlayerAdmin)