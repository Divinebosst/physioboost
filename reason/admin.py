from django.contrib import admin
from . models import Reason

# Register your models here.
class ReasonAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(Reason, ReasonAdmin)