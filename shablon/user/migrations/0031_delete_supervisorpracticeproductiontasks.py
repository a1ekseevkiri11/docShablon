# Generated by Django 5.0 on 2024-05-03 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_alter_ratingpracticestudent_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SupervisorPracticeProductionTasks',
        ),
    ]
