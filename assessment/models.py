from django.db import models
from players.models import Player
from injuries.models import Injuries
from bodyparts.models import BodyParts
from injurytype.models import InjuryType
from injurycause.models import InjuryCause
from injuryoccur.models import InjuryOccur
from injuryco.models import InjuryCo
from injuryviolation.models import InjuryViolation
from advicegiven.models import AdviceGiven
from diagnosis.models import Diagnosis
from severity.models import Severity
from actiontaken.models import ActionTaken
from injuryprevious.models import InjuryPrevious
from refereesanction.models import RefereeSanction
from referral.models import Referral
from protective_equipment.models  import ProtectiveEquipment
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Assessment(models.Model):
    name = models.CharField(max_length=100, default=None, null=True)
    surname = models.CharField(max_length=100, default=None, null=True)
    injured_body_parts = models.ManyToManyField(BodyParts)
    injury_type = models.ManyToManyField(InjuryType)
    other_injury = models.CharField(max_length=100, default=None, null=True)
    diagnosis = models.CharField(max_length=100, default=None, null=True)
    injury_previous = models.ManyToManyField(InjuryPrevious)
    injury_cause = models.ManyToManyField(InjuryCause)
    injury_occur = models.ManyToManyField(InjuryOccur)
    injury_occur_other = models.CharField(max_length=100, default=None, null=True)
    injury_co = models.ManyToManyField(InjuryCo)
    other_collision =  models.CharField(max_length=100, default=None, null=True)
    injury_violation = models.ManyToManyField(InjuryViolation)
    referee_sanction = models.ManyToManyField(RefereeSanction)
    advice_given = models.ManyToManyField(AdviceGiven)
    other_advice_given = models.CharField(max_length=100, default=None, null=True)
    severity = models.ManyToManyField(Severity)
    action_taken = models.ManyToManyField(ActionTaken)
    referral = models.ManyToManyField(Referral)
    other_referral = models.CharField(max_length=100, default=None, null=True)
    protective_equipment = models.ManyToManyField(ProtectiveEquipment)
    other_protective_equipment = models.CharField(max_length=100, default=None, null=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=18)
    
    def __str__(self):
        return self.name + " " + self.surname

    
    
