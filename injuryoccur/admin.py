from django.contrib import admin
from . models import InjuryOccur

# Register your models here.
class InjuryOccurAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryOccur, InjuryOccurAdmin)