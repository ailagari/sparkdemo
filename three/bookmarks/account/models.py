from audioop import minmax
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils.translation import gettext as _
from project.models import Project


class Activity(models.Model):
    name = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='Activities')
    date = models.DateField(_("Date"), default=datetime.date.today)
    start_time = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
    stop_time = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f'Project named {self.name} '