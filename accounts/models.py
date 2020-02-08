from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)

