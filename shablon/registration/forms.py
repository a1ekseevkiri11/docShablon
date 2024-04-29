from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from supervisorOPOP.models import (
    SupervisorOPOP,
)
from supervisorPractice.models import (
    SupervisorPractice,
)
from student.models import (
    Student,
    Group,
)

class StudentRegistrationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('group',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            student = Student.objects.create(user=user, group=self.cleaned_data['group'])
        return user
    

class SupervisorOPOPRegistrationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            supervisorOPOP = SupervisorOPOP.objects.create(user=user)
        return user



class SupervisorPracticeRegistrationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
    

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            supervisorPractice = SupervisorPractice.objects.create(user=user)
        return user