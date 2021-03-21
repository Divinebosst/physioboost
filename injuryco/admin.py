from django.contrib import admin
from . models import InjuryCo

# Register your models here.
class InjuryCoAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryCo, InjuryCoAdmin)