import django_filters
from django import forms

from user.models import (
    PracticeStudent,
    Practice,
    Group,
    DirectionOfTraining,
    
)

from .queryset import (
    get_queryset_direction_of_training_for_SupervisorPractice,
    get_queryset_group_for_SupervisorPractice,
)


class PracticeStudentFilter(django_filters.FilterSet):

    remark = django_filters.ModelChoiceFilter(
        field_name='remark',
        queryset=PracticeStudent.objects.all(),
        empty_label="Не оценены",
        label="Оценки",
    )

    group = django_filters.ModelMultipleChoiceFilter(
        to_field_name='title',
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Группы",
    )

    direction_of_training = django_filters.ModelMultipleChoiceFilter(
        to_field_name='title',
        queryset=DirectionOfTraining.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Направления подготовки",
    )



    class Meta:
        model = PracticeStudent
        fields = [
            'direction_of_training', 
            'group', 
            'remark',
        ]


    def __init__(self, *args, **kwargs):
        self.supervisorpractice = kwargs.pop('supervisorpractice', None)  # Получаем пользователя из kwargs
        super().__init__(*args, **kwargs)
        self.filters['direction_of_training'].queryset = get_queryset_direction_of_training_for_SupervisorPractice(self.supervisorpractice)
        self.filters['group'].queryset = get_queryset_group_for_SupervisorPractice(self.supervisorpractice)