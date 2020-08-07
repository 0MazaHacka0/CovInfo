from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from . import managers


class Patient(AbstractUser):
    username = None
    email = models.EmailField(_('email'), unique=True)

    objects = managers.PatientManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    notification_date = models.DateField()
    status = models.CharField(max_length=50)
