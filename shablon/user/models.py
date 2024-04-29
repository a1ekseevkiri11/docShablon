import os
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

def generate_upload_path(instance, filename):
    today = datetime.now()
    path = os.path.join('uploads', today.strftime('%Y/%m/%d'))
    return os.path.join(path, filename)


class Report(models.Model):


    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to=generate_upload_path)


    def __str__(self):
        return self.user.username
