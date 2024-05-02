import os
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


from registration.models import Profile

class AbstractSupervisor(Profile):
    post = models.CharField(max_length=256, null=True)
    class Meta:
        abstract = True

class SupervisorOPOP(AbstractSupervisor):
    pass


class SupervisorPractice(AbstractSupervisor):
    pass


class Institute(models.Model):


    title = models.CharField(max_length=256, unique=True)


    def __str__(self):
        return self.title
    

class DirectionOfTraining(models.Model):
    

    title = models.CharField(max_length=256, unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    supervisorOPOP = models.ManyToManyField(SupervisorOPOP)

    def __str__(self):
        return self.title
    

class Group(models.Model):


    level_choices = (
        ('Bachelor', 'Бакалавриат'),
        ('Specialist', 'Специалитет'),
        ('Master', 'Магистратура'),
        ('PhD', 'Аспирантура'),
    )

    title = models.CharField(max_length=10)
    direction_of_training = models.ForeignKey(DirectionOfTraining, on_delete=models.CASCADE, null=True)
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
    

    
class Practice(models.Model):


    type_choices = (
        ('type1', 'преддипломная'),
        ('type2', 'ознакомительная'),
        ('type2', 'технологическая'),
        ('type2', 'производственна'),
        ('type2', 'научно-исследовательская'),
    )

    kind_choices = (
        ('kind1', 'учебная'),
        ('kind2', 'производственная'),
    )


    title = models.CharField(max_length=512, unique=True)
    group = models.ManyToManyField(Group)
    type = models.CharField(max_length=20, choices=type_choices)
    kind = models.CharField(max_length=20, choices=kind_choices)
    date_start = models.DateField()
    date_end = models.DateField()

    #документ
    number_decree = models.CharField(max_length=20)
    date_decree = models.DateField()

    #адрес
    title_place = models.CharField(max_length=512, null=True)
    adress_place = models.CharField(max_length=512, null=True)

    #связь руководителей практики
    supervisor_practice = models.ForeignKey(SupervisorPractice, on_delete=models.SET_NULL, null=True)

    #руководителя от ЮГУ
    fio_supervisor_YuSU = models.CharField(max_length=512, null=True)
    post_supervisor_YuSU = models.CharField(max_length=512, null=True)

    #руководитель от организации
    fio_supervisor_company = models.CharField(max_length=512, null=True)
    post_supervisor_company = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title
    




class PracticeStudent(models.Model):
    type_choices = (
        ('long_term', 'долгосрочный'),
        ('краткосрочный', 'краткосрочный'),
    )

    rating_choices = (
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, null=True)
    production_tasks = models.TextField(null=True)
    type = models.CharField(max_length=20, choices=type_choices)
    pay = models.BooleanField()
    hard_quality =  models.TextField(null=True)
    quality =  models.TextField(null=True)
    amount = models.ForeignKey(Amount, on_delete=models.SET_NULL, null=True)
    remark = models.TextField(null=True)
    rating = models.CharField(max_length=2, choices=rating_choices, null=True)
    
    def __str__(self):
        return "Отчет " + self.practice.title


def generate_upload_path(instance, filename):
    today = datetime.now()
    path = os.path.join('uploads', today.strftime('%Y/%m/%d'))
    return os.path.join(path, filename)

