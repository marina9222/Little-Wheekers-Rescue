# Generated by Django 5.1.2 on 2024-11-21 19:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0005_remove_adoption_number_of_guinea_pigs'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='number_of_guinea_pigs',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]