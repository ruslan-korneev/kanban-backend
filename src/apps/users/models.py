from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser

from src.apps.users.const import UserRoles


class User(AbstractUser):
    role = models.PositiveSmallIntegerField(
        choices=UserRoles.choices, default=UserRoles.MEMBER
    )
