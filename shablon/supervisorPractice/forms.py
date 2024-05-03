from django import forms
from django.forms import DateInput

from user.models import (
    SupervisorPracticeProductionTasks,
    RatingPracticeStudent,
    
)


class PracticeStudentFormSupervisorPractice(forms.ModelForm):
    class Meta:
        model = RatingPracticeStudent
        fields = [
            'type',
            'pay',
            'hard_quality',
            'quality',
            'amount',
            'remark',
            'rating',
        ]

