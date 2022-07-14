# Generated by Django 4.0.1 on 2022-07-13 19:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_project_spend_project_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='stop_time',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
    ]