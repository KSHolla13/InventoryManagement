from django.db import models
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    Store_Name = models.CharField(max_length=200, blank=False)