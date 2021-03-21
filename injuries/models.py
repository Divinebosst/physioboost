from django.db import models
from django.contrib.auth.models import User
from severity.models import Severity
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from random import randint

# Create your models here.
class Injuries(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    symptoms = models.TextField(max_length=500)
    diagnostic_tests = models.TextField(max_length=500)
    classification = models.ForeignKey(Severity, max_length=500, on_delete=models.DO_NOTHING, null=True, default=None, blank=True)
    healing = models.TextField(max_length=500)
    complications = models.TextField(max_length=500)
    treatment = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(default=None, unique=True)
    
    def __str__(self):
        return self.id

    def __str__(self):
        return self.name

    def description_snippet(self):
        return self.description[:9] + '...'
    
    def symptoms_snippet(self):
        return self.symptoms[:9] + '...'

    def diag_snippet(self):
        return self.diagnostic_tests[:9] + '...'

    def healing_snippet(self):
        return self.healing[:6] + '...'

    def complications_snippet(self):
        return self.complications[:6] + '...'

    def treatment_snippet(self):
        return self.treatment[:6] + '...'
    
    def save(self, *args, **kwargs):
        if Injuries.objects.filter(name=self.name).exists():
            extra = str(randint(1,10))
            self.slug = slugify(self.name) + "-" + extra
        else:
            self.slug = slugify(self.name)
        super(Injuries, self).save(*args, **kwargs)



    def save(self, *args, **kwargs):
        if self.slug:
            origname = Injuries.objects.get(slug=self.slug).name
            if self.name == origname:
                super(Injuries, self).save(*args, **kwargs)
            elif Injuries.objects.filter(name=self.name).exists():
                extra = str(randint(1,100))
                self.slug = slugify(str(self.name)) + "-" + extra
                super(Injuries, self).save(*args, **kwargs)
        else:
            if Injuries.objects.filter(name=self.name).exists():
                extra = str(randint(1,100))
                self.slug = slugify(str(self.name)) + "-" + extra
                super(Injuries, self).save(*args, **kwargs)
            else:
                self.slug = slugify(str(self.name))
                super(Injuries, self).save(*args, **kwargs)