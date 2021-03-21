from django import forms
from . import models

class AddPlayer(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['name', 'surname', 'date_of_birth', 'nationality', 'address','height', 'weight', 'preferred_foot', 'position', 'jersey_number', 'strengths', 'weaknesses', 'club', 'image']

        widgets = {
            'name' : forms.TextInput(attrs={'id': 'first_name', 'class': 'validate'}),
            'surname' : forms.TextInput(attrs={'id': 'last_name', 'class': 'validate'}),
            'date_of_birth' : forms.TextInput(attrs={'id': 'date', 'class': 'datepicker'}),
            'nationality' : forms.TextInput(attrs={'id': 'nationality', 'class': 'validate'}),
            'address' : forms.TextInput(attrs={'id': 'address', 'class': 'validate'}),
            'height' : forms.NumberInput(attrs={'id': 'height', 'class': 'validate'}),
            'weight' : forms.NumberInput(attrs={'id': 'weight', 'class': 'validate'}),
            'preferred_foot' : forms.Select(attrs={'id': 'preferred_foot', 'class': 'validate'}),
            'position' : forms.Select(attrs={'id': 'position', 'class': 'validate'}),
            'jersey_number' : forms.NumberInput(attrs={'id': 'jersey_number', 'class': 'validate'}),
            'strengths' : forms.TextInput(attrs={'id': 'strengths', 'class': 'validate'}),
            'weaknesses' : forms.TextInput(attrs={'id': 'weaknesses', 'class': 'validate'}),
            'club' : forms.Select(attrs={'id': 'club', 'class': 'validate'}),
            'image' : forms.FileInput(attrs={'id': 'image','type' :'file', 'class' : 'dropify', 'data-height':'100'}),
        }

class EditStatus(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['status']