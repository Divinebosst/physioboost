from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from clubs.models import Club

# Create your models here.
class Cart(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.DO_NOTHING, default=None)
    order_number = models.CharField(max_length=100, default=None, null=True)
    
    def __str__(self):
        return self.name + " " + self.surname

    
    
