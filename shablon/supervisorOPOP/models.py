from django.db import models
from registration.models import Profile


class SupervisorOPOP(Profile):
    pass


class Place(models.Model):
    title = models.CharField(max_length=512, unique=True)
    adress = models.CharField(max_length=512)

    def __str__(self):
        return self.title


class Practice(models.Model):


    type_choices = (
        ('type1', 'Тип 1'),
        ('type2', 'Тип 2'),
    )

    kind_choices = (
        ('kind1', 'Вид 1'),
        ('kind2', 'Вид 2'),
    )


    title = models.CharField(max_length=512, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=type_choices)
    kind = models.CharField(max_length=20, choices=kind_choices)
    date_start = models.DateField()
    date_end = models.DateField()

    number_decree = models.CharField(max_length=20, choices=kind_choices)
    date_decree = models.DateField()
    
    #TODO добавить Руководителя практики от ЮГУ + Руководитель практики от предприятия

    def __str__(self):
        return self.title
