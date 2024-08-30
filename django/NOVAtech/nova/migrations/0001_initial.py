# Generated by Django 5.0.7 on 2024-08-26 11:19

import django.db.models.deletion
import nova.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestDeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(default=None, upload_to=nova.models.upload_to_timestamp)),
            ],
        ),
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('mobile', 'Mobile'), ('case', 'Case'), ('headphone', 'Headphone'), ('watch', 'Watch'), ('gadget', 'Gadget'), ('laptop', 'Laptop'), ('battery', 'Battery'), ('electronics', 'Electronics')], default='electronics', max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('actual_price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('image1', models.ImageField(upload_to=nova.models.upload_to_timestamp)),
                ('image2', models.ImageField(upload_to=nova.models.upload_to_timestamp)),
                ('image3', models.ImageField(upload_to=nova.models.upload_to_timestamp)),
            ],
        ),
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nova.productdata')),
            ],
        ),
    ]