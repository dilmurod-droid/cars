# Generated by Django 5.0.6 on 2024-07-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_remove_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=100000000000),
        ),
    ]
