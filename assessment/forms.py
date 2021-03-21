from django import forms
from . import models
from bodyparts.models import BodyParts
from injurytype.models import InjuryType
from injurycause.models import InjuryCause
from injuryoccur.models import InjuryOccur
from injuryco.models import InjuryCo
from injuryviolation.models import InjuryViolation
from advicegiven.models import AdviceGiven
from severity.models import Severity
from actiontaken.models import ActionTaken
from injuryprevious.models import InjuryPrevious
from refereesanction.models import RefereeSanction
from referral.models import Referral
from protective_equipment.models  import ProtectiveEquipment

class AddAssessment(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddAssessment, self).__init__(*args, **kwargs)
    class Meta:
        model = models.Assessment
        fields = ['injured_body_parts', 'injury_type', 'other_injury', 'diagnosis', 'injury_cause', 'injury_occur', 'injury_co','injury_violation', 'advice_given', 'severity', 'action_taken', 'injury_previous', 'other_collision', 'referee_sanction', 'injury_occur_other', 'other_advice_given', 'referral','other_referral', 'protective_equipment', 'other_protective_equipment']

        widgets = {
            'other_injury' : forms.TextInput(attrs={'id': 'other_injury', 'class': 'validate'}),
        }


    injured_body_parts = forms.ModelMultipleChoiceField(
        queryset=BodyParts.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_type = forms.ModelMultipleChoiceField(
        queryset=InjuryType.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_cause = forms.ModelMultipleChoiceField(
        queryset=InjuryCause.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_occur = forms.ModelMultipleChoiceField(
        queryset=InjuryOccur.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_co = forms.ModelMultipleChoiceField(
        queryset=InjuryCo.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_violation = forms.ModelMultipleChoiceField(
        queryset=InjuryViolation.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    advice_given = forms.ModelMultipleChoiceField(
        queryset=AdviceGiven.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    severity = forms.ModelMultipleChoiceField(
        queryset=Severity.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    action_taken = forms.ModelMultipleChoiceField(
        queryset=ActionTaken.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    injury_previous = forms.ModelMultipleChoiceField(
        queryset=InjuryPrevious.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    referee_sanction = forms.ModelMultipleChoiceField(
        queryset=RefereeSanction.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    referral = forms.ModelMultipleChoiceField(
        queryset=Referral.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    protective_equipment = forms.ModelMultipleChoiceField(
        queryset=ProtectiveEquipment.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )











        