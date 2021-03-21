from django.contrib import admin
from . models import AdviceGiven

# Register your models here.
class AdviceGivenAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(AdviceGiven, AdviceGivenAdmin)