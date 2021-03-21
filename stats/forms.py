from django import forms
from . import models

class AddStats(forms.ModelForm):
    class Meta:
        model = models.Stats
        fields = ['goals', 'assists']
