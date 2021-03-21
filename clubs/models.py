from django.db import models
from leagues.models import Leagues
# Create your models here.
class Club(models.Model):
    name  = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', blank=True)
    league = models.ForeignKey(Leagues, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.name