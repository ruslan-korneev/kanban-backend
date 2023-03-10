from django.db import models


class Board(models.Model):
    SLUG_MAX_LENGTH = 3

    title = models.CharField(max_length=24)
    slug = models.CharField(max_length=SLUG_MAX_LENGTH)
    description = models.CharField(max_length=24)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    statuses = models.ManyToManyField("tasks.TaskStatus")

    def save(self, *args, **kwargs) -> None:
        if not self.pk and not self.slug:
            self.slug = self.title[: self.SLUG_MAX_LENGTH].upper()
        return self.save(*args, **kwargs)


class Label(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField()
    color = models.CharField(max_length=6, default="000000")
    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)
