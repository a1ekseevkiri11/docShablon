# Generated by Django 5.0 on 2024-05-02 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_remove_group_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='number',
            new_name='title',
        ),
    ]
