from django.contrib import admin
from django.contrib.auth.models import Permission
from . models import Injuries

# Register your models here.
class InjuriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'symptoms', 'diagnostic_tests', 'classification', 'healing', 'complications', 'treatment')
    search_fields = ('name', 'description')

admin.site.register(Injuries, InjuriesAdmin)
admin.site.register(Permission)