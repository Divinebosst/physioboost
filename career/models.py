from django.db import models
from clubs.models import Club
from players.models import Player

# Create your models here.
class CareerHistory(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year = models.DateField(auto_now_add=True)
    seasons_played = models.PositiveIntegerField()