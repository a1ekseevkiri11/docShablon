from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):


    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
    )
    patronymic = models.CharField(max_length=256)


    class Meta:
        abstract = True
        

    def __str__(self):
        return self.user.username

