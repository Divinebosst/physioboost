from django.db import models
from clubs.models import Club
from status.models import Status
from foot.models import Foot
from position.models import Position
import re
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from random import randint
from datetime import date            

# Create your models here.
STATUS = 2
class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, default=None)
    address = models.CharField(max_length=200, default=None)
    date_of_birth = models.DateField(null=True, default=None)
    age = models.PositiveIntegerField(null=True, default=None)
    height = models.DecimalField(decimal_places=2, max_digits=3, default=None)
    weight = models.DecimalField(decimal_places=2, max_digits=5, default=None)
    club = models.ForeignKey(Club, on_delete=models.DO_NOTHING, default=None)
    preferred_foot = models.ForeignKey(Foot, on_delete = models.DO_NOTHING, default=None)
    position = models.ForeignKey(Position, on_delete = models.DO_NOTHING, default=None)
    jersey_number = models.PositiveIntegerField(null=True, default=None)
    strengths = models.CharField(max_length=100, default=None)
    weaknesses = models.CharField(max_length=100, default=None)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, default=STATUS, null=False)
    image = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(default=None, unique=True)
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.surname

    def save(self, *args, **kwargs):
        if self.slug:
            origname = Player.objects.get(slug=self.slug).name
            origsurname = Player.objects.get(slug=self.slug).surname
            if self.name == origname:
                if self.surname == origsurname:
                    super(Player, self).save(*args, **kwargs)
                elif Player.objects.filter(name=self.name).exists() & Player.objects.filter(surname=self.surname).exists():
                    extra = str(randint(1,10))
                    self.slug = slugify(str('%s %s' % (self.name, self.surname))) + "-" + extra
                    super(Player, self).save(*args, **kwargs)
        else:
            if Player.objects.filter(name=self.name).exists() & Player.objects.filter(surname=self.surname).exists():
                extra = str(randint(1,10))
                self.slug = slugify(str('%s %s' % (self.name, self.surname))) + "-" + extra
                super(Player, self).save(*args, **kwargs)

            else:
                self.slug = slugify(str('%s %s' % (self.name, self.surname)))
                super(Player, self).save(*args, **kwargs)


        if self.date_of_birth:
            def calculate_age(born):
                today = date.today()
                return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

            self.age = calculate_age(self.date_of_birth)
            super(Player, self).save(*args, **kwargs)

        