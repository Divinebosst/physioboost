from django.contrib import admin
from . models import Diagnosis

# Register your models here.
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('code','name');
    search_fields = ('code','name')

admin.site.register(Diagnosis, DiagnosisAdmin)