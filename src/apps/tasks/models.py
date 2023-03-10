from django.contrib.postgres.fields import ArrayField
from django.db import models

from src.apps.tasks.const import (
    REFERENCE_ID_MIN_LENGTH,
    REFERENCE_ID_CHARS,
    MAXIMUM_PRS,
    TaskStatusTypes,
)


class TaskStatus(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    type = models.PositiveSmallIntegerField(choices=TaskStatusTypes.choices)


class Task(models.Model):
    reference_id = models.CharField(
        max_length=64, editable=False, null=True, blank=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    board = models.ForeignKey(
        "boards.Board", on_delete=models.PROTECT, related_name="tasks"
    )
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )
    status = models.ForeignKey(
        "tasks.TaskStatus", on_delete=models.PROTECT, related_name="tasks"
    )
    children = models.ManyToManyField("self", symmetrical=False, related_name="parent")
    related_tasks = models.ManyToManyField("self")
    assignee = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
    )
    reviewers = models.ManyToManyField("users.User", related_name="tasks_to_review")
    labels = models.ManyToManyField("boards.Label")
    pull_requests = ArrayField(base_field=models.URLField(), size=MAXIMUM_PRS)

    def save(self, *args, **kwargs) -> None:
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            if not self.pk and not self.reference_id:
                self.reference_id = self.__generate_reference_id()
            super().save(update_fields=("reference_id",))

    def __generate_reference_id(self):
        """Generate a reference id which is shorter than id number"""
        counter = self.pk + len(REFERENCE_ID_CHARS) ** REFERENCE_ID_MIN_LENGTH
        reference_id = ""
        while counter:
            reference_id += REFERENCE_ID_CHARS[counter % len(REFERENCE_ID_CHARS)]
            counter //= len(REFERENCE_ID_CHARS)
        reference_id = reference_id[::-1] or REFERENCE_ID_CHARS[0]
        return f"{self.board.slug}-{reference_id}"
