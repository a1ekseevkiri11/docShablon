# Generated by Django 5.0 on 2024-05-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_alter_studentproductiontasks_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingpracticestudent',
            name='type',
            field=models.CharField(choices=[('long_term', 'долгосрочный'), ('short_term', 'краткосрочный')], max_length=20),
        ),
    ]