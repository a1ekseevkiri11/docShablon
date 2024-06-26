# Generated by Django 5.0 on 2024-05-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_remove_group_direction_of_training_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='supervisoropop',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='supervisoropop',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='supervisorpractice',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='supervisorpractice',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='patronymic',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='supervisoropop',
            name='patronymic',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='supervisorpractice',
            name='patronymic',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
