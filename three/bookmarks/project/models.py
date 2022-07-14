from audioop import minmax
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils.translation import gettext as _


class Project(models.Model):
    assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Projects')
    name = models.CharField(max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name