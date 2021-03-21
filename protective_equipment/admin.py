from django.contrib import admin
from . models import ProtectiveEquipment

# Register your models here.
class ProtectiveEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(ProtectiveEquipment, ProtectiveEquipmentAdmin)