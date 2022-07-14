# Generated by Django 4.0.1 on 2022-07-13 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_spend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='spend',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
