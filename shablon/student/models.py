from django.db import models
from registration.models import Profile
from supervisorOPOP.models import (
    SupervisorOPOP,
    Practice,
)

class Institute(models.Model):


    title = models.CharField(max_length=256, unique=True)


    def __str__(self):
        return self.title



class DirectionOfTraining(models.Model):
    

    title = models.CharField(max_length=256, unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    supervisorOPOP = models.ForeignKey(SupervisorOPOP, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    

class Group(models.Model):


    level_choices = (
        ('Bachelor', 'Бакалавриат'),
        ('Specialist', 'Специалитет'),
        ('Master', 'Магистратура'),
        ('PhD', 'Аспирантура'),
    )


    title = models.CharField(max_length=256)
    number = models.CharField(max_length=10)
    direction_of_training = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE)
    level = models.CharField(max_length=20, choices=level_choices)
    year = models.PositiveIntegerField()


    def __str__(self):
        return self.title


class Student(Profile):

    group =  models.ForeignKey(Group, on_delete=models.CASCADE)






class Amount(models.Model):

    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class PracticeStudent(models.Model):
    type_choices = (
        ('type1', 'Тип 1'),
        ('type2', 'Тип 2'),
    )

    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    practice =  models.ForeignKey(Practice, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=20, choices=type_choices)
    pay = models.BooleanField()
    hard_quality =  models.TimeField()
    quality =  models.TimeField()
    amount = models.ForeignKey(Amount, on_delete=models.SET_NULL, null=True)
    remark = models.TimeField()
    #TODO добавить руководителя практики от организации
    
    def __str__(self):
        return self.title
