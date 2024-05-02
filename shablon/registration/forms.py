from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from user.models import (
    Student,
    Group,
    SupervisorPractice,
    SupervisorOPOP,
)

class ProfileRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=False, help_text='Имя')
    last_name = forms.CharField(required=False, help_text='Фамилия')
    patronymic = forms.CharField(required=False, help_text='Отчество')


class StudentRegistrationForm(ProfileRegistrationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'last_name', 'first_name',  'patronymic', 'group', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student.objects.create(user=user, group=self.cleaned_data['group'])
        return user
    

class SupervisorOPOPRegistrationForm(ProfileRegistrationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'last_name', 'first_name',  'patronymic', 'password1', 'password2')


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            supervisorOPOP = SupervisorOPOP.objects.create(user=user)
        return user



class SupervisorPracticeRegistrationForm(ProfileRegistrationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'last_name', 'first_name',  'patronymic', 'password1', 'password2')
    

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            supervisorPractice = SupervisorPractice.objects.create(user=user)
        return user