# Generated by Django 5.0 on 2024-04-30 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DirectionOfTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('number', models.CharField(max_length=10)),
                ('level', models.CharField(choices=[('Bachelor', 'Бакалавриат'), ('Specialist', 'Специалитет'), ('Master', 'Магистратура'), ('PhD', 'Аспирантура')], max_length=20)),
                ('year', models.PositiveIntegerField()),
                ('direction_of_training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.directionoftraining')),
            ],
        ),
        migrations.AddField(
            model_name='directionoftraining',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.institute'),
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, unique=True)),
                ('type', models.CharField(choices=[('type1', 'Тип 1'), ('type2', 'Тип 2')], max_length=20)),
                ('kind', models.CharField(choices=[('kind1', 'Вид 1'), ('kind2', 'Вид 2')], max_length=20)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('number_decree', models.CharField(choices=[('kind1', 'Вид 1'), ('kind2', 'Вид 2')], max_length=20)),
                ('date_decree', models.DateField()),
                ('title_place', models.CharField(default=None, max_length=512, unique=True)),
                ('adress_place', models.CharField(default=None, max_length=512)),
                ('group', models.ManyToManyField(to='user.group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(max_length=256)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PracticeStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('type1', 'Тип 1'), ('type2', 'Тип 2')], max_length=20)),
                ('pay', models.BooleanField()),
                ('hard_quality', models.TimeField()),
                ('quality', models.TimeField()),
                ('remark', models.TimeField()),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.amount')),
                ('practice', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.practice')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
        migrations.CreateModel(
            name='SupervisorOPOP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='practice',
            name='supervisorOPOP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.supervisoropop'),
        ),
        migrations.AddField(
            model_name='directionoftraining',
            name='supervisorOPOP',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.supervisoropop'),
        ),
        migrations.CreateModel(
            name='SupervisorPractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
