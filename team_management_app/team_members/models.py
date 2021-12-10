from django.db import models
from django import forms
from django.urls import reverse

ROLES = ((False, "Regular"), (True, "Admin"))

class TeamMember(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    is_admin = models.BooleanField(choices=ROLES, default=False)