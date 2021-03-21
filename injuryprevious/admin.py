from django.contrib import admin
from . models import InjuryPrevious

# Register your models here.
class InjuryPreviousAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryPrevious, InjuryPreviousAdmin)