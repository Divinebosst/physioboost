from django.contrib import admin
from . models import RefereeSanction

# Register your models here.
class RefereeSanctionAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(RefereeSanction, RefereeSanctionAdmin)