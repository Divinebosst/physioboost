from django.contrib import admin
from . models import Club

# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(Club, ClubAdmin)