from django.db import models
from players.models import Player 
from clubs.models import Club 
from season.models import Season
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Stats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, default=None)
    goals = models.PositiveIntegerField(null=True, default=None)
    assists = models.PositiveIntegerField(null=True, default=None)
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, default=1)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING, default=None, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
    date_added = models.DateTimeField(verbose_name='date added', auto_now_add=True, null=True)

    def __str__(self):
        return self.player_id
