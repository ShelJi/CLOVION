# Generated by Django 5.1 on 2024-09-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personmodel',
            name='empty',
            field=models.CharField(default='hee', max_length=50),
            preserve_default=False,
        ),
    ]
