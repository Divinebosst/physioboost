from django import forms
from . import models

class AddInjuries(forms.ModelForm):
    class Meta:
        model = models.Injuries
        fields = ['name', 'description', 'symptoms', 'diagnostic_tests', 'classification', 'healing','complications', 'treatment', 'image']
        widgets = {
            
            'description' : forms.Textarea(attrs={'id': 'description', 'class':'materialize-textarea'}),
            'symptoms' : forms.TextInput(attrs={'id': 'symptoms'}),
            'diagnostic_tests' : forms.TextInput(attrs={'id': 'diagnostic_tests'}),
            'complications' : forms.TextInput(attrs={'id': 'complications'}),
            'treatment' : forms.TextInput(attrs={'id': 'treatment'}),
            'healing' : forms.TextInput(attrs={'id': 'healing'}),
            'image' : forms.FileInput(attrs={'id': 'image','type' :'file', 'class' : 'dropify', 'data-height':'100'}),
        }