from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):


    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    patronymic = models.CharField(max_length=64, null=True)



    class Meta:
        abstract = True
        

    def __str__(self):
        return self.user.username

