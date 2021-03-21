from django.contrib import admin
from . models import InjuryViolation

# Register your models here.
class InjuryViolationAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryViolation, InjuryViolationAdmin)