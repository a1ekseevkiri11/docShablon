from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import m2m_changed

from student.models import Group


class Profile(models.Model):


    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )
    patronymic = models.CharField(max_length=256)


    class Meta:
        abstract = True
        

    def __str__(self):
        return self.user.username



class Student(Profile):


    group =  models.ForeignKey(Group, on_delete=models.CASCADE)


class SupervisorPractice(Profile):
    pass


class SupervisorOPOP(Profile):
    pass

