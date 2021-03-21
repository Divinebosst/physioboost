from django.contrib import admin
from . models import InjuryActivity

# Register your models here.
class InjuryActivityAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(InjuryActivity, InjuryActivityAdmin)