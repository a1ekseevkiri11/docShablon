from django.db import models

class Institute(models.Model):


    title = models.CharField(max_length=256, unique=True)


    def __str__(self):
        return self.title



class DirectionOfTraining(models.Model):


    title = models.CharField(max_length=256, unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)

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