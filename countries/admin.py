from django.contrib import admin
from . models import Countries

# Register your models here.
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(Countries, CountriesAdmin)