# Generated by Django 5.0 on 2024-05-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_productiontasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicestudent',
            name='hard_quality',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='practicestudent',
            name='quality',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='practicestudent',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]