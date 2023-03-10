from django.db import models


REFERENCE_ID_CHARS = "FRY708QVDCL9ABWOH14EJ2UZ6IP5KTXGM3NS"
REFERENCE_ID_MIN_LENGTH = 6  # Reference ID minimal length

MAXIMUM_PRS = 10  # max amount of pull requests links bind to task


class TaskStatusTypes(models.IntegerChoices):
    BACKLOG = 0, "Backlog"
    TODO = 1, "TODO"
    WIP = 2, "Work In Progress"
    REVIEW = 3, "Code Review"
    TESTING = 4, "Testing"
    DONE = 5, "Done"
    CANCELLED = 6, "Cancelled"
