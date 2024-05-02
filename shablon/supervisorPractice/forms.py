from django import forms
from django.forms import DateInput

from user.models import (
    Practice,
    PracticeStudent,
    Group,
    DirectionOfTraining
)


class PracticeStudentFormSupervisorPractice(forms.ModelForm):
    class Meta:
        model = PracticeStudent
        fields = [
            'hard_quality',
            'quality',
            'amount',
            'remark',
            'rating',
        ]

