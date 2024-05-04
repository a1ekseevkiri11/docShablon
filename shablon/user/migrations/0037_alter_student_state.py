# Generated by Django 5.0 on 2024-05-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_student_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(choices=[('no', 'нет'), ('part-time', 'декретный отпуск'), ('extramural', 'академический отпуск')], default='no', max_length=512),
        ),
    ]