from django.db import models


class UserRoles(models.IntegerChoices):
    MEMBER = 0, "Member"
    DEVELOPER = 1, "Developer"
    LEAD = 2, "Team Lead"
    MANAGER = 3, "Project Manager"
    ADMIN = 4, "Administrator"
