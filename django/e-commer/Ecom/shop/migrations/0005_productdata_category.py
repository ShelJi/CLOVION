# Generated by Django 5.0.7 on 2024-08-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productdata_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
    ]