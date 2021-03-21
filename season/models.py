from django.db import models

# Create your models here.
class Season(models.Model):
    name = models.CharField(max_length = 50)
    started_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.id

    def __str__(self):
        return self.name