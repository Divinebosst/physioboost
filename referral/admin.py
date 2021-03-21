from django.contrib import admin
from . models import Referral

# Register your models here.
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('name',);
    search_fields = ('name',)

admin.site.register(Referral, ReferralAdmin)