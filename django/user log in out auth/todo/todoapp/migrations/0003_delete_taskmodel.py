# Generated by Django 5.0.7 on 2024-08-11 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_taskmodel_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskModel',
        ),
    ]
