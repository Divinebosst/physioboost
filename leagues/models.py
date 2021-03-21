from django.db import models
from countries.models import Countries

# Create your models here.
class Leagues(models.Model):
    name  = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING, default=None)
    image = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name