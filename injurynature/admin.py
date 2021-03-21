from django.contrib import admin
from . models import InjuryNature

# Register your models here.
class InjuryNatureAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryNature, InjuryNatureAdmin)