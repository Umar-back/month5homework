from django.db import models
from django.contrib.auth.models import User


class Confirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()





