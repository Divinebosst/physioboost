from django.db import models

# Create your models here.
class Dataset(models.Model):
    age = models.CharField(max_length=100)
    weight = models.DecimalField(decimal_places=2, max_digits=5, default=None)
    height = models.DecimalField(decimal_places=2, max_digits=3, default=None)
    classification = models.CharField(max_length=100, null=True)
