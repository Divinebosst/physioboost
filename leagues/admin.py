from django.contrib import admin
from . models import Leagues

# Register your models here.
class LeaguesAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(Leagues, LeaguesAdmin)