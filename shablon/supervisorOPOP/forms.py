from django import forms
from django.forms import DateInput

from user.models import (
    Practice,
    Group,
    DirectionOfTraining
)

from .queryset import(
    get_queryset_group_for_SupervisorOPOP
)



class PracticeForm(forms.ModelForm):

    group = forms.ModelMultipleChoiceField(
        queryset=Group.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    def __init__(self, supervisoropop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].queryset = get_queryset_group_for_SupervisorOPOP(supervisoropop)

    class Meta:
        model = Practice
        fields = [
            'title',
            'group',
            'type',
            'kind',
            'date_start',
            'date_end',
            'number_decree',
            'date_decree',
            'title_place',
            'adress_place'
        ]
        widgets = {
            'date_start': DateInput(attrs={'type': 'date'}),
            'date_end': DateInput(attrs={'type': 'date'}),
            'date_decree': DateInput(attrs={'type': 'date'}),
        }