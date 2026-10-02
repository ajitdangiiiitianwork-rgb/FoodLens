from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  pass

class UserPreference(models.Model):
  user = models.OneToOneField(
    User,
    on_delete = models.CASCADE,
    related_name = 'preferences'
  )

  dietary_preference = models.CharField(max_length=100, blank=True, null=True)
  budget_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  budget_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  favourite_cuisines = models.TextField(blank=True)
  max_distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
