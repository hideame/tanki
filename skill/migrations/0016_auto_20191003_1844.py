# Generated by Django 2.2.4 on 2019-10-03 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0015_auto_20191003_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=5000, validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(9999900)]),
        ),
    ]
