from django.contrib import admin
from . models import ActionTaken

# Register your models here.
class ActionTakenAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(ActionTaken, ActionTakenAdmin)