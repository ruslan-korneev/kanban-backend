from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=24)
    description = models.CharField(max_length=24)
    board = models.ForeignKey("boards.Board", on_delete=models.PROTECT)
    lead = models.ForeignKey("users.User", on_delete=models.PROTECT)
    start = models.DateField()
    end = models.DateField()
