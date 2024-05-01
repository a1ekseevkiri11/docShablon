from django import forms
from django.forms import DateInput

from user.models import (
    Practice,
    PracticeStudent,
    Group,
    DirectionOfTraining
)

class PracticeStudentFormStudent(forms.ModelForm):
    class Meta:
        model = PracticeStudent
        fields = [
            'type',
            'pay',
        ]