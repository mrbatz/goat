from django.db import models
from django.contrib.auth.models import User


class UserProfileInfoForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username
