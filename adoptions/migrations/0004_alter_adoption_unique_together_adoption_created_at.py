# Generated by Django 5.1.2 on 2024-10-29 15:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_delete_adopter'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adoption',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='adoption',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]