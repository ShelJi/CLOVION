# Generated by Django 5.0.7 on 2024-08-29 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0009_remove_reviewmodel_reviewproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nova.reviewmodel'),
        ),
    ]