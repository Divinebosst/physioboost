from django.db import models
from players.models import Player
from status.models import Status
# Create your models here.
class StatusHistory(models.Model):
    player = models.ForeignKey(Player, on_delete=models.DO_NOTHING, default=None)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=None)
    date = models.DateTimeField(auto_now_add=True)
